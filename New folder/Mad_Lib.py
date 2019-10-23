#Daniel Embley
#9/9
#Mad libs

#Please enter a noun
#Please enter a verb
#Please enter a adjective

noun = input("Enter a noun")
noun2 = input("Enter a noun")
verb = input("Enter a noun")
verb2 = input("Enter a verb")
verb3 = input("Enter a painful verb")
adj = input("Enter an adjective")
liquid = input("Enter a liquid")
liquid2 = input("Enter a liquid")
angerType = input("Describe a type of anger")
harmType = input("Describe a type of harm")


text = str.format("""Jack and Jill
Went up the {}
To fetch a pail of {}
Jack {} down
And broke his {}
And Jill came {} after.Up Jack got
And home did trot
As fast as he could {}
And went to bed
And plastered his head
With {}and {}  paper. When Jill came in
How she did grin
To see Jack's paper plaster;
Mother {}
Did {} her next
For causing Jack's disaster.""", noun, noun2, verb, verb2, verb3, adj, liquid, liquid2, angerType, harmType)

print(text)


input()
