
import smtplib

def calculateStats(numbers):
    computedNumbers = {}
    if not numbers:
        computedNumbers["avg"] = float('nan')
        computedNumbers["max"] = float('nan')
        computedNumbers["min"] = float('nan')
    try:
        computedNumbers["avg"] = sum(numbers)/len(numbers)
        computedNumbers["max"] = max(numbers)
        computedNumbers["min"] = min(numbers)
    except Exception as e:
        print("Exception occured:", e)
    
    return computedNumbers

class EmailAlert:
    def __init__(self):
        self.emailSent = False
        
    def sendEmail(self, msg):
        try:
            s = smtplib.SMTP('localhost')
            s.sendmail("dummyMail@gmail.com", "dummyMail@gmail.com", msg)
            s.quit()
            print ("Email sent successfully!")
            self.emailSent = True
        except Exception as ex:
            print ("Error: email was not sent…",ex)

class LEDAlert:
    def __init__(self):
        self.ledGlows = False
    def glowLed(self, msg):
        self.ledGlows = True
            
class StatsAlerter:
    def __init__(self, maxThreshold, Alert):
        self.maxThreshold = maxThreshold
        self.emailAlert = Alert[0]
        self.ledAlert = Alert[1]
    
    def checkAndAlert(self, maxListValues):
        print("------Inside Check Alert func----")
        maxvalue = max(maxListValues)
        if maxvalue > self.maxThreshold:
            self.emailAlert.sendEmail("Max value {0} is greater than threshold {1}".format(maxvalue, self.maxThreshold ))
            self.ledAlert.glowLed("Max value {0} is greater than threshold {1}".format(maxvalue, self.maxThreshold ))
         
