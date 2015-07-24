import time
from duolingo import duolingo

def getUsers():
        ''' Reads line-separated TXT file of users and stores each one in our username map '''

        file = open('usernames.txt', 'r')
        rawUsers = file.readlines()

        # Loops through the scraped list and removes extra whitespace
        usernames = map(lambda x:x.rstrip(),rawUsers)

        file.close()

        return usernames

def getScores(usernames):
        ''' Takes in Map of usernames and appends their Duolingo scores to scores.txt '''
        #Open scores.txt and write scores
        output = open('scores.txt', 'a')
        output.write("\n==============================================")
        output.write("Date & Time of Last Run " + time.strftime("%c"))
        output.write("==============================================\n\n")
        for user in usernames:
                lingo = duolingo.Duolingo(user)
                languages = lingo.get_languages()
                output.write(user+":\n")
                for lang in languages:
                        output.write(lang)
                        langDetails = lingo.get_language_details(lang)
                        output.write("(Level: "+str(langDetails['level'])+")")
                        output.write(" - [Score: "+str(langDetails['points'])+"]")
                        output.write("\n")
                output.write("\n\n")
        output.close()

def main():
        users = getUsers()
        getScores(users)

if __name__ == '__main__':
        main()
