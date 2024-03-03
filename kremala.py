#------------------------------------------------  kremala.py------------------------------------------------#
"""Αυτό ειναι το κυρίως πρόγραμμα, εδώ χρησιμοποιούνται όλες οι συναρτήσεις ώστε να λειτουργει ομαλά το παιχνίδι."""

from inputs import * 
from outputs import *
from greek_dictionary import *

welcome_message()           #Εμφάνιση του "intro" του παιχνιδιού
n_players=get_number()      #Αποθήκευση του αριθμού των παιχτών, 
if n_players==1:
    Singleplayer=True       #Σε περίπτωση που παίζει μόνο ένας παίχτης, θα υπάρχει μόνο ενας γύρος, που είτε θα νικήσει, είτε θα χάσει.
else:
    Singleplayer=False
names=get_names(n_players)  #Αποθήκευση των ονομάτων των παιχτών
game_is_on=True             #H μεταβλητή θα είναι Τrue καθ'όλη τη διάρκεια του παιχνιδιού (για να γίνουν όσοι γύροι χρειαστούν.)
round=1                     #Μετρητής των γύρων
last_used_words=['','']     #Aρχικοποίηση μίας λίστας 2 στοχειών, όπου κατα τη διάρκεια του παιχνιδιού θα αποθηκεύονται σε αυτή οι 2 πιο πρόσφατες χρησιμοποιημένες λέξεις.
while game_is_on:           #Όσο δηλαδή δεν υπάρχει νικητής, ή όσο δεν έχουν χάσει όλοι, το παιχνίδι θα συνεχίζεται.
    new_names=[]            #Σε αυτή τη λίστα θα εκχωρούμε τα ονόματα των παιχτών που θα νικάνε όταν έρχεται η σειρά τους και θα προχωρούν στον επόμενο γύρο.
    round_message(round)    #Εμφάνιση του αριθμού του γύρου.
    for player in range(n_players):                 #Παίζουν όλοι οι παίχτες που βρίσκονται στο συγκεκριμένο γύρο.
        print('Παίζει ο παίχτης : '+names[player])
        level_of_difficulty=get_difficulty()        #Ζητείται απο τον παίχτη να δώσει τη δυσκολία του, ώστε να έχει αντίστοιχες ζωές.
        if level_of_difficulty=='Αρχάριος':
            lives=8
        elif level_of_difficulty=='Μέτριος':
            lives=6
        elif level_of_difficulty=='Έμπειρος':
            lives=4
        print('Προσοχή, έχεις περιθώριο να επιλέξεις μέχρι',lives-1,'λάθος γράμματα \nκαι στο '+str(lives)+'ο λάθος γράμμα σου θα βγεις εκτός παιχνιδιού.')
        word=pick_random_word(last_used_words)                  #Επιλέγεται μία τυχαία λέξη, η οποία δεν έχει εμφανιστεί στους 2 τελευταίους γύρους
        last_used_words=used_words_update(word,last_used_words) #Ενημερώνεται η λίστα των πιο πρόσφατων λέξεων προσθέτοντας την καινούργια.    
        hidden_word=['_' for i in range(0,len(word))]           #Δημιουργούμε μία λίστα με '_' όσα και τα γράμματα της λέξης που ψάχνουμε.
        print_hidden(hidden_word)                               #Τυπώνεται η "κρυφή λέξη"
        won_round , died =False , False
        while won_round==False and died==False:                 #Ο παίκτης θα παίζει μέχρι να νικήσει, ή "κρεμαστεί".
            letter_guessed=get_guess()                          #Ο παίχτης κάνει τη μαντεψιά του
            found_a_letter=False                                
            if letter_guessed=='σ':                             #Η μόνη ακραία περίπτωση στην επιλογή σύμφωνου είναι το σίγμα τελικό.               
                for i in range(0,len(word)):
                    if word[i]=='σ':
                        hidden_word[i]='σ'
                        found_a_letter=True
                    elif word[i]=='ς':
                        hidden_word[i]='ς'
                        found_a_letter=True
                if found_a_letter:
                    print('Σωστή μαντεψιά!')
                    print_hidden(hidden_word)
            elif (letter_guessed in consonants) and (letter_guessed in word):  #Η πιο απλή περίπτωση είναι ο παίχτης να μάντεψε ΣΩΣΤΑ κάποιο σύμφωνο
                found_a_letter=True
                print('Σωστή μαντεψιά!')
                for i in range(0,len(word)):
                    if letter_guessed==word[i]:
                        hidden_word[i]=letter_guessed
                print_hidden(hidden_word)          
            elif letter_guessed in vowels:      #H πιο σύνθετη περίπτωση είναι ο παίχτης να μάντεψε φωνήεν, όπου λάβονται υπόψιν οι τόνοι.
                temp=vowels.index(letter_guessed)   #Πρώτα εντοπίζεται η θέση του φωνήεντος στη λίστα των φωνηέντων
                if temp%2==0:         #Έτσι όπως ειναι κατασκευασμένη η λίστα των φωνηέντων, στις άρτιες θέσεις είναι αυτά χωρίς τόνους.
                    for i in range(0,len(word)):        #Αν μαντέψει σωστά ένα φωνήεν γράφοντας το χωρίς τόνο, πρέπει να εμφανιστεί
                        if word[i]==vowels[temp]:       #όπου υπάρχει και με τόνο.
                            hidden_word[i]=vowels[temp]
                            found_a_letter=True
                        if word[i]==vowels[temp+1]:
                            hidden_word[i]=vowels[temp+1]
                            found_a_letter=True
                else:               #Αντίστοιχα, σε περίπτωση που ο χρήστης μάντεψε ένα σωστό φωνήεν γράφοντας το με τόνο, πρέπει να εμφανιστεί 
                    for i in range(0,len(word)):    #και εκει που δεν έχει τονο μέσα στη λέξη.
                        if word[i]==vowels[temp]:
                            hidden_word[i]=vowels[temp]
                            found_a_letter=True
                        if word[i]==vowels[temp-1]:
                            hidden_word[i]=vowels[temp-1]
                            found_a_letter=True
                if found_a_letter:
                    print('Σωστή μαντεψιά!')
                    print_hidden(hidden_word)
            if found_a_letter==False:
                lives-=1                            
                show_hangingman(lives,level_of_difficulty)
                if lives==0:
                    print('Λυπάμαι, αλλά κάηκες! Βγαίνεις εκτός παιχνιδιού')
                    print('Η λέξη που ψάχναμε ήταν: ',word)
                    died=True
                    if Singleplayer:        
                        print('Έχασες. Καλύτερη τύχη την επόμενη φορά.')
                        game_is_on=False
                else:
                    if lives==1:
                        print('Έχεις ακόμα '+str(lives)+' ζωή.')
                    else:
                        print('Έχεις ακόμα '+str(lives)+' ζωές.')
                    print_hidden(hidden_word)
            if '_' not in hidden_word: #Όταν ο παίχτης μαντέψει σωστά όλα τα γράμματα, ειτε προκρίνεται στον επόμενο γύρο.
                if Singleplayer:        #είτε κερδίζει αν παίζει μόνος του και τελειώνει το παιχνίδι.
                    print(names[0],'νίκησες το παιχνίδι! Μπράβο!')
                    print('Βρήκες σωστά τη λέξη:',word)
                    game_is_on=False
                    won_round=True
                else:
                    print('Συγχαρητήρια! Νίκησες σε αυτό το γύρο.') #Αν το παιχνίδι είναι πολλαπλών παιχτών συνεχίζεται.
                    print('Βρήκες σωστά τη λέξη:',word)
                    won_round=True
                    new_names.append(names[player]) #Το όνομα του παίχτη που προκρίνεται στον επόμενο γύρο αποθηκεύται σε νέα λίστα.
                    print('════════════════════════════════════════════')
    names=new_names     
    n_players=len(names)
    if (not Singleplayer and len(names)==1):
        print('Ο νικητής του παιχνιδιού ειναι ο/η: '+names[0]+'!!!') 
        game_is_on=False
    elif (not Singleplayer and len(names)==0):
        print('Δε νίκησε κανείς το παιχνίδι αυτή τη φορά.')
        game_is_on=False
    else:           #Αν υπάρχουν τουλάχιστον 2 άτομα στο παιχνίδι, προχωράνε στον επόμενο γύρο.
        round+=1       
input('Πάτησε ENTER για να τερματίσεις το πρόγραμμα.')

                    
                    
                  
                    
                
                
            
                        
