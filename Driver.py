#! python3

import re, pyperclip, csv

class crawler():

    def __init__(self):
        print('Crawler initialised')

    # Verbose allows for triple quotes/multi-line string
    phoneRegex = re.compile(r'''
    # Area code(optional)
    (
    (\d\d\d\d)?
    # Space separator
    (\s | -)
    # first 3 digits
    \d\d\d
    # space separator
    (\s | -)
    # last 4 digits
    \d\d\d\d)
    ''', re.VERBOSE)

    emailRegex = re.compile(r'''
    # First part before @ symbol
    [a-zA-Z0-9._]+
    
    # @ symbol
    @
    
    # Domain email
    [a-zA-Z0-9.]+
    ''', re.VERBOSE)


    def extractData(self):
        rawText = pyperclip.paste()

        extractedNumbers = self.phoneRegex.findall(rawText)
        extractedEmails = self.emailRegex.findall(rawText)
        allNumbers = []
        allEmails = []

        for phone in extractedNumbers:
            allNumbers.append(phone[0])

        for email in extractedEmails:
            allEmails.append(email)

        choice = input('CSV or Txt file format?')

        if choice == 'CSV' or choice == 'csv': self.outputCSV(allEmails, allNumbers)
        elif choice == 'Txt' or choice == 'txt': self.outputData(allEmails, allNumbers)

    def outputData(self, foundEmails, foundPhones):
        output_file = open('ExtractedData.txt', 'w')
        output_file.write('Numbers found from clipboard \n')

        for phone in foundPhones:
            output_file.write(phone + '\n')

        output_file.write('Emails found from clipboard \n')

        for email in foundEmails:
            output_file.write(email + '\n')

        output_file.close()

    def outputCSV(self, foundEmails, foundPhones):
        with open('Details.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Phone Number'])
            for phone in foundPhones:
                writer.writerow([phone])

            writer.writerow(['Email Address'])
            for email in foundEmails:
                writer.writerow([email])



crawler = crawler()
crawler.extractData()
print('Crawler Finished')
