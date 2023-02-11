from youtube import YoutubeDataAPIClient


if __name__ == "__main__":
    res = YoutubeDataAPIClient().fetch_url_as_list("SHOWROOM", 1)
    print("\n".join(res))
