import logging, random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def papiello(update, context):
    prefix = prefix_list[random.randint(0, len(prefix_list)-1)]
    pokemon = context.args[0].capitalize()

    if pokemon in pokemon_list or pokemon == 'Donalla':
        sentence = prefix + ' ' + format_sentence(pokemon)
    else:
        sentence = 'Non esiste ' + pokemon + ' qui a Volla...'

    update.message.reply_text(sentence)

def format_sentence(pokemon):
    sentence_array = [
        'Trovo che ' + pokemon + ' abbia una sessualità giocosa',
        'Provo una certa idiosincrasia per ' + pokemon,
        'Il moveset di ' + pokemon + ' genera troppo rumore statistico',
        pokemon + ' ha una sua cinestetica',
        'Ritengo ' + pokemon + ' vagamente interessante',
        pokemon + ' poco si addice alla mia personalità',
        'Comprendo che chi gioca ' + pokemon + ' possa divertirsi di più. Alla fine non gioca diversamente da come giocava prima con la differenza che con la dmax usata bene può scalare ancora più velocemente. Secondo me, ripeto, il problema sorge guardando al gioco come ad un gioco posizionale. Se la ultra era - vagamente - vicina agli scacchi, o a go, o a qualsiasi altro gioco in cui la posizione si costruisce, qua la posizione non puoi svilupparla. O la becchi a t1 o addio',
        'Comunque per quanto trovo che sia le z che le dyna siano meccaniche innaturali e brutte...' + pokemon + ' è molto peggio. E sì, la questione "coverage" è uno dei motivi. La z coverage era molto rara e, se vi ricordate, ai novizi la prima cosa che dicevamo era "non giocate le z senza stab". Era sensato perché la z la giochi una volta e soprattutto la tieni fissa su un pokemon. Se dai la z lotta a lunala te la tieni per tutta la bo3 e sostanzialmente giochi senza Z. Con la dyna è diverso: la coverage non stab la giochi più volentieri perché 1) mal che vada dynamaxi altro 2) ok, faccio poco danno ma almeno tolgo la rain/prendo il boost in speed/vattelapesca',
        'Un team con '+ pokemon + ' ha delle idee di build interessanti che potrebbe valere la pena approfondire: 1) inci senza la mossa fuoco ma con roar 2) lando mixed spreaddato per fare la z fisica/speciale in base a se era intimidito o no'
        'Comunque c\'era un ragazzo con una ragazza, uno di quelli che poi non ha giocato, a cui ho scambiato un ' + pokemon + ' con distortozona, un bisharp stolascelta e un abomasnow, più altra mazzamma gennata la settimana prima della pc, pur di farlo giocare perché era senza pokemon. Mi fa: "vorrei togliere distortozona a questo gengar, posso farlo? Ti regalo una squama cuore così gliela rimetti". Non ho avuto il coraggio di dirgli che erano pokemon gennati a muzzo dieci minuti prima, era tutto felice. Mi voleva offrire addirittura un caffè. Poi ha fatto: "se mi becchi sul battlespot con un abomasnow sappi che è il tuo"'
    ]

    return sentence_array[random.randint(0, len(sentence_array)-1 )]

def load(filename):
    txt_file = open(filename, "r")
    list_array = []
    for row in txt_file:
        list_array.append(row[:-1])
    
    txt_file.close()
    return list_array

def main():
    print("Starting up bot...")

    #loading pokemon name files
    print("Loading pokemons...")
    global pokemon_list
    pokemon_list = load('pokemon.txt')

    #loading prefix sentences
    print("Loading prefix sentences...")
    global prefix_list
    prefix_list = load('premesse.txt')

    print("listening...")
    token_file = open("token.txt", "r")
    updater = Updater(token_file.read().rstrip("\n"), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("papiello", papiello))
    updater.start_polling()
    updater.idle()         

if __name__ == '__main__':
    main()