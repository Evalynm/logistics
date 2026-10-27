#store lots

#data structures
#list, set, tuple ,dictionary

#1.list
people = ["john","michael","maria","hussein","jane"]
scores = [34,45,79,66,71,12,90,30]

print(people[3])
print(scores[0])
print(people[-1])#last name

#people.append("nuggi") #adding a name
print(people)
#scores.append(11) #adding a number
#print(scores)

#people.clear()
#people.sort()
#scores.sort(reverse=True)
#print(people)
#print(scores)

#print(scores[0], scores[-1])
#print(sum(scores)/len(scores))
#scores.count(34)
#print(scores.count(34))

scores.sort()
#slicing
print(scores)
print(scores[-2:]) #top two list
print(scores[:3]) #lowwer numbers
print(scores[3:5])

#2.sets -- remove duplicates
numbers = {87,89,87,67,54}
print(numbers)
numbers.add(57) #add numbers
print(numbers)

#3.tuple
days = ("mon","tue","wed","thur","fri","sat","sun")
print(days)

#4.dictionary
person = {"name","zillow","city:","marsabit","age:",19}
print(person)

#data structures + algorithms
print(sum(numbers))

watu = [{"name": "sila","age":22},{"name": "Hin","age":59},{"name": "cril","age":16}]
print(watu[2])
