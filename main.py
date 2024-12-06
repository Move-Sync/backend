from app import app  # app.py から app をインポート

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,  # 環境変数 PORT を使わず、デフォルトで 5000 を指定
        debug=True  # デバッグモードを True に設定
    )
