import os

from apiclient.discovery import build
from dotenv import load_dotenv

load_dotenv(verbose=True)


class YoutubeDataAPIClient:
    """
    Youtube data APIのラッパークラス
    https://developers.google.com/youtube/v3/docs?hl=ja
    """
    API_KEY = os.environ.get("API_KEY")
    # 動画のurlは下のbase urlにvideoId付与したもの
    BASE_URL = "https://www.youtube.com/watch?v="

    def __init__(self) -> None:
        self._client = build("youtube", "v3", developerKey=self.API_KEY)

    def fetch_url_as_list(
        self,
        query: str,
        num_fetched: int,
        order: str = "date",
        region_code: str = None,
        published_after: str = None,
        max_try: int = 10
    ) -> list[str]:
        page_token = None
        res_urls = []

        max_result = 50 if num_fetched > 50 else num_fetched

        for _ in range(max_try):
            # quota引っかかる可能性があるためAPI実行上限いれておく
            res = self._client.search().list(
                # https://developers.google.com/youtube/v3/docs/search/list?hl=ja
                part="id",
                # 検索したい文字列を指定
                q=query,
                order=order,
                type="video",
                maxResults=max_result,
                pageToken=page_token,
                regionCode=region_code,
                publishedAfter=published_after,
                fields="nextPageToken,items(id(videoId))"
            ).execute()

            page_token = res["nextPageToken"]

            items = res["items"]
            if not items:
                continue
            res_urls.extend(
                [f'{self.BASE_URL}{r["id"]["videoId"]}' for r in items])

            if len(res_urls) >= num_fetched or page_token is None:
                # urlが指定した件取得できるか、検索結果がでなくまで繰り返す
                break

        return res_urls
