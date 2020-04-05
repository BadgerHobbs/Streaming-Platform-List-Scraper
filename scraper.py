import json, time
import urllib.request

# Links

# Movies

# Netflix
Netflix_Movies = "https://api.reelgood.com/v3.0/content/browse/source/netflix?availability=onSources&content_kind=movie&hide_seen=false&hide_tracked=false&hide_watchlisted=false&imdb_end=10&imdb_start=0&override_user_sources=true&overriding_free=false&overriding_sources=netflix&region=us&rt_end=100&rt_start=0&skip=%s&sort=0&sources=netflix&take=250&year_end=2020&year_start=1900"
# Hulu
Hulu_Movies = "https://api.reelgood.com/v3.0/content/browse/source/hulu?availability=onSources&content_kind=movie&hide_seen=false&hide_tracked=false&hide_watchlisted=false&imdb_end=10&imdb_start=0&override_user_sources=true&overriding_free=false&overriding_sources=hulu_plus&region=us&rt_end=100&rt_start=0&skip=%s&sort=0&sources=hulu_plus&take=250&year_end=2020&year_start=1900"
# Prime Video
PrimeVideo_Movies = "https://api.reelgood.com/v3.0/content/browse/source/amazon?availability=onSources&content_kind=movie&hide_seen=false&hide_tracked=false&hide_watchlisted=false&imdb_end=10&imdb_start=0&override_user_sources=true&overriding_free=false&overriding_sources=amazon_prime&region=us&rt_end=100&rt_start=0&skip=%s&sort=0&sources=amazon_prime&take=250&year_end=2020&year_start=1900"
# HBO
HBO_Movies = "https://api.reelgood.com/v3.0/content/browse/source/hbo?availability=onSources&content_kind=movie&hide_seen=false&hide_tracked=false&hide_watchlisted=false&imdb_end=10&imdb_start=0&override_user_sources=true&overriding_free=false&overriding_sources=hbo&region=us&rt_end=100&rt_start=0&skip=%s&sort=0&sources=hbo&take=250&year_end=2020&year_start=1900"
# Disney+
Disney_Movies = "https://api.reelgood.com/v3.0/content/browse/source/disney_plus?availability=onSources&content_kind=movie&hide_seen=false&hide_tracked=false&hide_watchlisted=false&imdb_end=10&imdb_start=0&override_user_sources=true&overriding_free=false&overriding_sources=disney_plus&region=us&rt_end=100&rt_start=0&skip=%s&sort=0&sources=disney_plus&take=250&year_end=2020&year_start=1900"

# TV Shows

# Netflix
Netflix_TVShows = "https://api.reelgood.com/v3.0/content/browse/source/netflix?availability=onSources&content_kind=show&hide_seen=false&hide_tracked=false&hide_watchlisted=false&imdb_end=10&imdb_start=0&override_user_sources=true&overriding_free=false&overriding_sources=netflix&region=us&rt_end=100&rt_start=0&skip=%s&sort=0&sources=netflix&take=250&year_end=2020&year_start=1900"
# Hulu
Hulu_TVShows = "https://api.reelgood.com/v3.0/content/browse/source/hulu?availability=onSources&content_kind=show&hide_seen=false&hide_tracked=false&hide_watchlisted=false&imdb_end=10&imdb_start=0&override_user_sources=true&overriding_free=false&overriding_sources=hulu_plus&region=us&rt_end=100&rt_start=0&skip=%s&sort=0&sources=hulu_plus&take=250&year_end=2020&year_start=1900"
# Prime Video
PrimeVideo_TVShows = "https://api.reelgood.com/v3.0/content/browse/source/amazon?availability=onSources&content_kind=show&hide_seen=false&hide_tracked=false&hide_watchlisted=false&imdb_end=10&imdb_start=0&override_user_sources=true&overriding_free=false&overriding_sources=amazon_prime&region=us&rt_end=100&rt_start=0&skip=%s&sort=0&sources=amazon_prime&take=250&year_end=2020&year_start=1900"
# HBO
HBO_TVShows = "https://api.reelgood.com/v3.0/content/browse/source/hbo?availability=onSources&content_kind=show&hide_seen=false&hide_tracked=false&hide_watchlisted=false&imdb_end=10&imdb_start=0&override_user_sources=true&overriding_free=false&overriding_sources=hbo&region=us&rt_end=100&rt_start=0&skip=%s&sort=0&sources=hbo&take=250&year_end=2020&year_start=1900"
# Disney+
Disney_TVShows = "https://api.reelgood.com/v3.0/content/browse/source/disney_plus?availability=onSources&content_kind=show&hide_seen=false&hide_tracked=false&hide_watchlisted=false&imdb_end=10&imdb_start=0&override_user_sources=true&overriding_free=false&overriding_sources=disney_plus&region=us&rt_end=100&rt_start=0&skip=%s&sort=0&sources=disney_plus&take=250&year_end=2020&year_start=1900"

def getData(source,output):

	print("Trying:",source)

	skip = 0
	take = 50

	print("Starting",output)

	f = open("download.txt","w", encoding='utf-8')
	f.write("")
	f.close()

	previousTotal = 0

	i = 0

	while True:

		link = source % str(skip)
		req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})      
		with urllib.request.urlopen(req) as response:
			result = json.loads(response.read().decode('utf-8'))

			f = open("download.txt","a", encoding='utf-8')
			strResult = str(result).split("},")

			if len(strResult) <= 2:
				break

			for line in strResult:
				if "'content_kind': None" in line:
				     continue
				tmpstr = line + "\n"
				#print(tmpstr)
				f.write(tmpstr)
				
			f.close()
			
			total = len(open("download.txt", encoding='utf-8').readlines(  ))
			print("Completed:",skip,"to",skip+take,"\t\t\tTotal Added:",total)

			if previousTotal == total:

				previousTotal = total
			
			skip = total

		i += 1
			
		time.sleep(0.1)

	print("\nScraping Complete")

	print("\nGenerating " + output + "...")

	f = open(output,"w", encoding='utf-8')
	f.write("")
	f.close()

	f = open("download.txt","r", encoding='utf-8')
	data = f.read().splitlines()
	f.close()

	movieList = []

	for line in data:
		#print(line)
		position = line.find("title") + 9

		if position < 1:

			position = line.find("title") + 9

		movieName = ""

		for characterInt in range(position,len(line)):

			try:
				if (line[characterInt] != "'") and (line[characterInt+1] != ","):

					movieName = movieName + line[characterInt]

				else:
					break

			except:
				break

		position = line.find("released_on") + 15

		movieDate = ""

		for characterInt in range(position,len(line)):

			try:
				if line[characterInt] != "-":

					movieDate = movieDate + line[characterInt]

				else:
					break

			except:
				break

		movieName = movieName.strip() + " (" + movieDate + ")\n"
		try:
			f = open(output,"a", encoding='utf-8')
			f.write(movieName)
			f.close()
		except:
			time.sleep(0.01)
			f = open(output,"a", encoding='utf-8')
			f.write(movieName)
			f.close()

	print("Done!",output,"\n")
        
getData(Netflix_Movies,"Netflix_Movies.txt")
getData(Hulu_Movies,"Hulu_Movies.txt")
getData(PrimeVideo_Movies,"PrimeVideo_Movies.txt")
getData(HBO_Movies,"HBO_Movies.txt")
getData(Disney_Movies,"Disney_Movies.txt")

getData(Netflix_TVShows,"Netflix_TVShows.txt")
getData(Hulu_TVShows,"Hulu_TVShows.txt")
getData(PrimeVideo_TVShows,"PrimeVideo_TVShows.txt")
getData(HBO_TVShows,"HBO_TVShows.txt")
getData(Disney_TVShows,"Disney_TVShows.txt")
    
