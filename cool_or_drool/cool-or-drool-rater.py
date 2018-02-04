import graphics as g

movieRatingsFile = None
while True:
    movieRatingsFileName = input("Enter the name of the ratings file: ")
    try:
        movieRatingsFile = open( movieRatingsFileName, "r" )
        break
    except FileNotFoundError:
        print("{0} was not found".format ( movieRatingsFileName ))
        

firstLine = movieRatingsFile.readline()
firstLineTokens = firstLine.split(",")
movieTitle = firstLineTokens[1]
printFoolieBadge = ""
totalRatings = 0
totalRatingsAboveCool = 0
higherIterator = 0
lowerIterator = 0
for line in movieRatingsFile:
    ratings = line.strip().split(",")
    countTen = ratings.count('10')
    countNine = ratings.count('9')
    countOne = ratings.count('1')
    countTwo = ratings.count('2')
    countTensAndNines = higherIterator + countTen + countNine
    countOneAndTwos = lowerIterator + countOne + countTwo
##    print(fooleRating)
    for i in range(countOne + countTwo):
        lowerIterator +=1 
    for x in range(countTen + countNine):
        higherIterator +=1 
    for rating in ratings:
        numericRating = int( rating )
        totalRatings += 1
        if numericRating >= 6:
            totalRatingsAboveCool += 1
coolPct = totalRatingsAboveCool / totalRatings
print(countTensAndNines)
print(countOneAndTwos)

percentOfStronglySplit = (countTensAndNines +  countOneAndTwos)/100
thresholdStronglySplit = abs(countOneAndTwos - countTensAndNines)
if percentOfStronglySplit >= .35 and thresholdStronglySplit <= 5:
     printFoolieBadge = "FOOLIE"
print('Movie Title: {}'.format( movieTitle ))
print('Total Number of Ratings: {}'.format( totalRatings ) )
print('Cool Percentage: {}'.format( coolPct ))


ratingImageFileName = ''
rating = ''
if totalRatings < 10:
    rating = "Too soon to rule"
    ratingImageFileName = 'tooSoonToRule.gif'
elif coolPct >= .6:
    rating = "COOL"
    ratingImageFileName = 'cool.gif'
else:
    rating = "DROOL"
    ratingImageFileName = 'drool.gif'
print( rating )
    
    

win = g.GraphWin('COOL or DROOL rater', 400, 400)

titleText = g.Text( g.Point( 200, 50 ), movieTitle )
titleText.draw( win )

ratingImage = g.Image( g.Point( 200, 200), ratingImageFileName )
ratingImage.draw( win )

coolPctText = g.Text( g.Point( 200, 350) , "{0:0.0f}% {1}".format( coolPct * 100, rating ))
coolPctText.draw( win )

foolieText = g.Text( g.Point( 200, 375) , printFoolieBadge)
foolieText.setTextColor('red')
foolieText.setSize(20)
foolieText.draw(win)

