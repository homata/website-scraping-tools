website-scraping-tools 
====

* [Python, Docker, Scrapyを使ってURLからWebページをHTML形式でダウンロードする](https://zenn.dev/elletech/articles/docker-python-spider-23y07m07d?utm_source=pocket_saves)
    * [sugayutokyo/docker-scrapy-spider](https://github.com/sugayutokyo/docker-scrapy-spider)
* [Python, scrapy でお祭りスクレイピング](https://qiita.com/takecore@github/items/35905779504016085801)
    * [takecore/festival-crawler](https://github.com/takecore/festival-crawler)

```
$ docker-compose up -d --build
$ docker-compose exec scrapy bash
```

```
/usr/src/app# scrapy startproject scraping .
/usr/src/app# scrapy genspider getHtml zenn.dev
```

```
$ scrapy crawl getHtml
```
