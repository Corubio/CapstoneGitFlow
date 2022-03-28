def retweetTop():
    with open('farmers-protest-tweets-2021-03-5.json', 'r') as tweets:
        
        top10 = []
        answer = 'TOP RETWEETED:\n'
        
        for i in range(0, 419507):
            tweet = tweets.readline().split(", ")
            url = tweet[0].split(": ")[1]
            for section in tweet:
                if "retweetCount" in section:
                    retweets = int(section.split(": ")[1])
                    if len(top10) < 10:
                        top10.append([url, retweets])
                    else:
                        last = min(top10, key = lambda k: k[1])
                        if retweets > last[1]:
                            for j in range(0, 10):
                                if top10[j] == last:
                                    top10[j] = [url, retweets]
                            
        top10.sort(key = lambda k: (k[1]), reverse = True)
        for i in range(0, 10):
            answer += f'\t{i + 1}° {top10[i][0]}; retweets: {top10[i][1]}\n'
        answer += "--------------"
        
        return (answer)

def tweetedTop():
    with open('farmers-protest-tweets-2021-03-5.json', 'r') as tweets:
        
        top10 = []
        answer = 'TOP TWEETERS:\n'
        
        for i in range(0, 419507):
            tweet = tweets.readline().split(", ")
            j = 0
            keep = True
            while keep:
                if '{"username": ' in tweet[j]:
                    userName = tweet[j].split(": ")[2]
                    keep = False
                    j = 0
                else:
                    j += 1
            keep = True
            while keep:
                if 'mediaCount' in tweet[j]:
                    mediaCount = int(tweet[j].split(": ")[1])
                    keep = False
                    j = 0
                else:
                    j += 1
            keep = True
            if len(top10) < 10:
                for k in range(0, len(top10)):
                    if top10[k][0] == userName:
                        keep = False
                if len(top10) < 1 or keep:
                        top10.append([userName, mediaCount])
            else:
                last = min(top10, key = lambda k: k[1])
                if mediaCount > last[1]:
                    for k in range(0, 10):
                        if top10[k][0] == userName:
                            keep = False
                    for k in range(0, 10):
                        if top10[k] == last and keep:
                            top10[k] = [userName, mediaCount]
                            
        top10.sort(key = lambda k: (k[1]), reverse = True)
        for i in range(0, 10):
            answer += f'\t{i + 1}° {top10[i][0]}; tweets: {top10[i][1]}\n'
        answer += "--------------"
        
        return (answer)
    
def dayTop():
    with open('farmers-protest-tweets-2021-03-5.json', 'r') as tweets:
        
        top10 = []
        answer = 'TOP DIAS:\n'
        
        for i in range(0, 419507):
            tweet = tweets.readline().split(", ")
            j = 0
            keep = True
            while keep:
                if 'date' in tweet[j]:
                    date = tweet[j].split(": ")[1].split("T")[0]
                    date = date[1 : len(date)]
                    keep = False
                    j = 0
                else:
                    j += 1
            keep = True
            if len(top10) < 1:
                    top10.append([date, 1])
            else:
                for k in range(0, len(top10)):
                    if top10[k][0] == date:
                        top10[k][1] = top10[k][1] + 1
                        keep = False
                        break
                if keep:
                    top10.append([date, 1])
            
                            
        top10.sort(key = lambda k: (k[1]), reverse = True)
        for i in range(0, 10):
            answer += f'\t{i + 1}° {top10[i][0]}; tweets: {top10[i][1]}\n'
        answer += "--------------"
        
        return (answer)
    
def hashtagTop():
    with open('farmers-protest-tweets-2021-03-5.json', 'r') as tweets:
        
        top10 = []
        answer = 'TOP HASHTAGS:\n'
        
        for i in range(0, 419507):
            tweet = tweets.readline().split(", ")
            j = 0
            keep = True
            while keep:
                if 'content' in tweet[j]:
                    hashtagsList = tweet[j].split(": ")[1].replace("\\n", " ").replace('"', '').split(" ")
                    hashtags = []
                    for k in hashtagsList:
                        if '#' in k:
                            hashtags.append(k)
                    keep = False
                    j = 0
                else:
                    j += 1
            keep = True
            if len(top10) < 1:
                    for k in hashtags:
                        top10.append([k, 1])
            else:
                for l in hashtags:
                    for k in range(0, len(top10)):
                        if top10[k][0] == l:
                            top10[k][1] = top10[k][1] + 1
                            keep = False
                            break
                    if keep:
                        top10.append([l, 1])
            
                            
        top10.sort(key = lambda k: (k[1]), reverse = True)
        for i in range(0, 10):
            answer += f'\t{i + 1}° {top10[i][0]}; tweets: {top10[i][1]}\n'
        answer += "--------------"
        
        return (answer)
    
print(retweetTop())
print(tweetedTop())
print(dayTop())
print(hashtagTop())