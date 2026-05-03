"""
AK Tool — YouTube Downloader Backend
Flask + yt-dlp
Run: python app.py
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp
import re

app = Flask(__name__)
CORS(app)  # Frontend ke liye CORS allow karo

# ─── YouTube URL validate ───────────────────────────────────────────────────
def is_yt_url(url: str) -> bool:
    return bool(re.search(r"(youtube\.com/watch|youtu\.be/)", url))


# ─── yt-dlp se video info lao ──────────────────────────────────────────────
def get_info(url: str) -> dict:
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "noplaylist": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(url, download=False)


# ─── Format list banana ─────────────────────────────────────────────────────
def build_formats(info: dict) -> dict:
    fmts = info.get("formats", [])

    # ── Video formats ──────────────────────────────────────────────
    video_map = {}
    target_heights = [1080, 720, 480, 360]

    for f in fmts:
        h   = f.get("height") or 0
        ext = f.get("ext", "")
        vco = f.get("vcodec", "none")
        aco = f.get("acodec", "none")

        if vco == "none" or not h:
            continue
        if h not in target_heights:
            continue

        # combined (audio+video) prefer karo
        has_audio = aco != "none"
        url_      = f.get("url", "")
        if not url_:
            continue

        if h not in video_map or (has_audio and not video_map[h]["has_audio"]):
            video_map[h] = {
                "quality"  : f"{h}p",
                "ext"      : "mp4",
                "url"      : url_,
                "has_audio": has_audio,
                "filesize" : f.get("filesize") or f.get("filesize_approx"),
                "fps"      : f.get("fps"),
            }

    videos = [video_map[h] for h in target_heights if h in video_map]

    # ── Audio formats ──────────────────────────────────────────────
    audio_list = []
    for f in fmts:
        aco = f.get("acodec", "none")
        vco = f.get("vcodec", "none")
        if aco == "none" or vco != "none":
            continue
        url_ = f.get("url", "")
        if not url_:
            continue
        audio_list.append({
            "abr"     : f.get("abr") or 0,
            "ext"     : f.get("ext", "m4a"),
            "url"     : url_,
            "filesize": f.get("filesize") or f.get("filesize_approx"),
        })

    audio_list.sort(key=lambda x: x["abr"], reverse=True)

    # Best aur standard audio
    audios = []
    if audio_list:
        best = audio_list[0]
        audios.append({
            "label"   : f"MP3 High Quality ({int(best['abr'])}kbps)" if best["abr"] else "MP3 High Quality",
            "ext"     : best["ext"],
            "url"     : best["url"],
            "filesize": best["filesize"],
        })
        # ~128kbps wala dhundho
        std = next((a for a in audio_list if 100 <= a["abr"] <= 145), None)
        if std and std["url"] != best["url"]:
            audios.append({
                "label"   : f"MP3 Standard ({int(std['abr'])}kbps)" if std["abr"] else "MP3 Standard",
                "ext"     : std["ext"],
                "url"     : std["url"],
                "filesize": std["filesize"],
            })
        elif len(audio_list) > 1:
            a2 = audio_list[1]
            audios.append({
                "label"   : f"MP3 Standard ({int(a2['abr'])}kbps)" if a2["abr"] else "MP3 Standard",
                "ext"     : a2["ext"],
                "url"     : a2["url"],
                "filesize": a2["filesize"],
            })

    return {"videos": videos, "audios": audios}


# ═══════════════════════════════════════════════════════════════════════════
#  ROUTES
# ═══════════════════════════════════════════════════════════════════════════

@app.route("/api/info", methods=["GET"])
def api_info():
    """
    GET /api/info?url=<youtube_url>
    Returns: title, thumbnail, video formats, audio formats
    """
    url = request.args.get("url", "").strip()
    if not url:
        return jsonify({"error": "URL parameter missing hai."}), 400
    if not is_yt_url(url):
        return jsonify({"error": "Sirf YouTube links support hote hain."}), 400

    try:
        info    = get_info(url)
        formats = build_formats(info)
        return jsonify({
            "title"    : info.get("title", "YouTube Video"),
            "thumbnail": info.get("thumbnail", ""),
            "duration" : info.get("duration"),          # seconds
            "uploader" : info.get("uploader", ""),
            "views"    : info.get("view_count"),
            "videos"   : formats["videos"],
            "audios"   : formats["audios"],
        })
    except yt_dlp.utils.DownloadError as e:
        msg = str(e)
        if "Private video" in msg:
            return jsonify({"error": "Yeh video private hai."}), 403
        if "This video is not available" in msg:
            return jsonify({"error": "Video available nahi hai."}), 404
        return jsonify({"error": "Video info nahi mili. URL check karein."}), 500
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "AK Tool Backend chal raha hai ✓"})


# ─── Run ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  AK Tool — YouTube Downloader Backend")
    print("  http://localhost:5000")
    print("=" * 50)
    app.run(host="0.0.0.0", port=5000, debug=True)
