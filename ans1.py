import argparse

from youtube import YoutubeDataAPIClient

parser = argparse.ArgumentParser()

# オプション引数（指定しなくても良い引数）を追加
parser.add_argument('--num_fetched', type=int, default=1)


args = parser.parse_args()


if __name__ == "__main__":
    res = YoutubeDataAPIClient().fetch_url_as_list("SHOWROOM", args.num_fetched)
    print("\n".join(res))
