import argparse
from datetime import datetime, timedelta, timezone

from youtube import YoutubeDataAPIClient

parser = argparse.ArgumentParser()

parser.add_argument('--num_fetched', type=int, default=1)

args = parser.parse_args()


if __name__ == "__main__":
    three_days_before = (datetime.now(timezone.utc) -
                         timedelta(days=3)).isoformat()

    # NOTE 人気を視聴数（viewCount）ととらえたが、評価の高い順（rating）かもしれない
    res = YoutubeDataAPIClient().fetch_url_as_list("Apex Legends", args.num_fetched,
                                                   order="viewCount", region_code="JP", published_after=three_days_before)
    print("\n".join(res))
