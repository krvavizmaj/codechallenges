import time

def theSmallestStringCipher(key, message):
    i = 0
    j = 0
    a = ""

    while len(key) < len(message):
        key += "{"
    while len(message) < len(key):
        message += "{"

    while i < len(key) and j < len(message):
        if key[i] < message[j]:
            a += key[i]
            i += 1
        elif message[j] < key[i]:
            a += message[j]
            j += 1
        else:
            a += key[i]
            if key[i+1:] < message[j:]:
                i += 1
            else:
                j += 1
    
    if i < len(key):
        a += key[i:]
    elif j < len(message):
        a += message[j:]

    return a.replace("{", "")

def theSmallestStringCipher1(key, message):
    s = [["" for _ in range(len(message) + 1)] for _ in range(len(key) + 1)]
    for i in range(1, len(message) + 1):
        s[0][i] = s[0][i-1] + message[i-1]
    for i in range(1, len(key) + 1):
        s[i][0] = s[i-1][0] + key[i-1]

    a = ""
    b = ""
    for i in range(1, len(key) + 1):
        for j in range(1, len(message) + 1):
            s[i][j] = min(s[i][j-1] + message[j-1], s[i-1][j] + key[i-1])

    return s[len(key)][len(message)]

key = "ofgmtjdaaxizmnuynotznjwfdttmxdkksvxtzrioenetkdqammxbmgmdyilyragoyagsnggyhteourgjgulgvzuujkesrltcendapzeihywpjxkupevuntjatktbfhorqqulgevtsbjjxllgzwgkctgfubeqtmreegjivxooyehezcjquedhsxrpcpcuwwjimpuxqzncvurktdvmiaaekeszczuxqknljneamqcgklirhlcgdbymejvykyquddpwjyjdjdsrtkttbeiwjxrwavbeddmtxeykjipmsidrrbkahmxwriqdxvfnxkanumzzhlxnhzswcqunytxlihiwsmwgexehfwikfycpfkncfibkgippshuvfxqffffswzxrrderxgaqqkfeyizijhfrzlaycbezyiauiczjxxndcqplpvajpcnmmowrjxshgsuglfvrspfxwlymkqouqyefwfcumepnagsidnknhiuyawbpbugucwshngplodrdkutdsqjhmsvnzolzxojhjehtmjaenimzbzoufjmydnuutuctrtkeacnsaibzhebcsmdduqpsyowkqqgzymmbduzpbbwwkmtygukooytrqvpqsxgpqcvmimdpqxoenwunywnnfljwyhaylekayqlmoowupbtejdzlzwhdpjbdydquitgcvcakndtpkcoxdmlkoqucdhedpblrpvbslyopgolgldrxoydafkdtxcbsfoweaauhgumellmjssmkvyqplxblojvyqhvuvmidjbdjaxqbcskgujhlavfyhmjojsthcsmwpgisgyiwcfoxjaifbdzmhbbbtbgvpnkucgglamuexkfbaaldzmugtipkkiakdtucwpdpmpvecjsqmbylcolstaxkceadicwalhznspouvvxuaksfhljbtfuyesanitwlfmosxrwcqhcxyvzfxogfckbenushmzhzihbrubpapfkdeqlwgkwutfoulowl"
message = "wqyfjnkyggaggkchjhkblikgrrqcymqhycepialfzzplizeyybmdztenlxeblnvqinsdkbumjemhngvxgmhkowxxuojtqzagiyfdkwswkcrtzncofcrmoszwkzayhlopaqacfamfgawswhdepzjsegrpvqyeuxmdrxfkjkqpzbrwcvxsyvgzxcogqspirxinpzsrukkrdrremipdwvcxjaxirbfemifliunbkvgcupokznpguaxnahuhumkwjavujdeapbvtgzcpzsrsewbzqepjivytyfpujagfsjdrizcredacnsktqwdhtynfucbbkxaqdxurbckqgugefdmbrtbhkdpjjvernppxhdrtgitshniwqyfywkjqkqhulkpfpvrnckrcsgbmeroxiwnjxjdnocqwtxflwtwugswsthhowifbolytwxbubmimcubbemevobbwlzzvzsiyfdhzotsoguacseyynyrlmnrzdqelsvcohsvoagsivjtacgbhvimlogugvvlortlgfsnahzgtiusglvlafwcxpxlidubayvgxljogsuqsuukqxcdyeconytetodjwvbvgugsusanvoethohdllhnrnqvibsulfelzfkpcvhdwwdamzsrasatswwuymyfpdyhmzyxpzlxiwnwrbkcinqabvcluzhwerrvechuuggogrniqdcgmizjccpbvdzelnnxvlifcagvrfgnftyvszdyveseeuozrcanjryxhleoydxrhcxjrfcozosxfepiknnfxnbaexmpktmdrdjycmyavwhukbmeycwyxxxyponfjbdbvmlunspilwsicunlqanroeqoantfzimmezqtuotspjttkficetucwnkkhqrdlfjmgbopnslaktpfyedcdlyyrmtnbxkdpoyqhrtcsmvkrwwaujcmyfpnkxhwodyzjlhfbmfnugazkzlvmjlfyfvbchytfkjmeftiaqplzljinnkfp"
# key = "abcba"
# message = "abcdcba"
# key = "b"
# message = "baa"
# key = "cbede"
# message = "cbede"

start = int(round(time.time() * 1000))
# print(theSmallestStringCipher(key, message))
print(theSmallestStringCipher1(key, message))
end = int(round(time.time() * 1000))
print(end - start)