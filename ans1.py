import argparse

from youtube import YoutubeDataAPIClient

parser = argparse.ArgumentParser()

parser.add_argument('--num_fetched', default=1)    # オプション引数（指定しなくても良い引数）を追加


args = parser.parse_args()


if __name__ == "__main__":
    res = YoutubeDataAPIClient().fetch_url_as_list("SHOWROOM", args.num_fetched)
    print("\n".join(res))
