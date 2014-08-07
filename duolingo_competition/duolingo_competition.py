import time
from duolingo import duolingo

def getUsers():
        # Get our users from a text file
        # each user is on its own line

        global users
        
        file = open('usernames.txt', 'r')
        rawUsers = file.readlines()

        usernames = map(lambda x:x.rstrip(),rawUsers)

        file.close()

        return usernames

def getScores():
        #Open scores.txt and write scores
        output = open('scores.txt', 'a')
        output.write("\n==============================================")
        output.write("Date & Time of Last Run " + time.strftime("%c"))
        output.write("==============================================\n\n")
        for user in usernames:

                lingo = duolingo.Duolingo(user)
                languages = lingo.get_languages()
                output.write(user+":\n")
                #output.write("\n".join(languages))
                for lang in languages:
                        output.write(lang)
                        langDetails = lingo.get_language_details(lang)
                        output.write("(Level: "+str(langDetails['level'])+")")
                        output.write(" - [Score: "+str(langDetails['points'])+"]")
                        output.write("\n")
                output.write("\n\n")

        output.close

def main():
        users = getUsers()
        writeScores = getScores(users)

if __name__ == '__main__':
        main()
