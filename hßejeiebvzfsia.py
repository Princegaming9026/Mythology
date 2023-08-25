



Name = input("What is your Name: ")
print('\x1b[5;32;m Hi ',Name)

Phone = input('\x1b[5;35;47m Enter your phone number:+91')
             
             
print("Thanks ....")


File = input("[0] Know about mythology             [1] research on peoples               ")
if File == ("0"):
    print('\033[2;43;36m Mythology refers to a collection of myths, stories, and legends that are often rooted in the beliefs, traditions, and cultural practices of different societies. These myths usually involve supernatural beings, gods, heroes, and other elements that explain natural phenomena, historical events, or the origins of the world and humanity. Mythologies come from various cultures around the world, and each culture has its own unique set of myths and stories that provide insights into their values, beliefs, and worldview. Some well-known mythologies include: Greek Mythology: The myths of ancient Greece feature gods and goddesses such as Zeus, Hera, Apollo, Athena, and many others. These myths explain various aspects of the world and human experiences. Norse Mythology: Originating in the Scandinavian region, Norse mythology includes figures like Odin, Thor, and Loki. The stories often center around the struggles of gods and mortals against cosmic forces. Egyptian Mythology: The myths of ancient Egypt involve deities like Ra, Osiris, Isis, and Anubis. They reflect the complex religious and cosmological beliefs of the Egyptian civilization. Hindu Mythology: Hindu mythology includes a vast array of gods and goddesses like Vishnu, Shiva, and Lakshmi. These myths are deeply intertwined with religious practices in India. Chinese Mythology: Chinese mythology features beings like the Jade Emperor, the Monkey King, and various legendary creatures. These myths are often connected to philosophical concepts and cultural traditions. Native American Mythology: The indigenous peoples of the Americas have their own rich mythologies, with stories of spirits, creation, and interactions with the natural world. African Mythology: The diverse cultures of Africa have their own mythologies, which vary widely across regions and ethnic groups. These myths often relate to the origin of people, animals, and natural features. Celtic Mythology: Originating in the Celtic-speaking regions of Europe, Celtic myths involve deities like Lugh and Brigid, as well as legends of heroes and magical creatures. ')
 
if File == ("1"):
    print("'\x1b[5;32;m ok ")
    A = input('\033[2;33;41m type the first word in capital latter which you are going to research     >>> ')
    if A == ("A"):
        print('\x1b[1;33;45;m What you want to know ')
        passing = input("[0] Know about birth                 [1] God                              [2] Dygree                           [3] Nature                           " )
        if passing == ("0"):
         print('\x1b[3;36;43m the birth between 21 march to  19 april ')
        if passing == ("1"):
         print('\x1b[3;36;43m mars')
        if passing == ("2"):
         print('\x1b[3;36;43m (0°≤ λ <30°)')
        if passing == ("3"):
         print('\x1b[3;36;43m Aries people are independent minded. They have their own different views on right and wrong. They have amazing leadership skills and believe in making their own way. The people of Aries do not keep anything in their mind and do what they say. ')
        if passing == ("00"):
         print("ok")










