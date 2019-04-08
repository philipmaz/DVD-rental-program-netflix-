#dane=[[1,'Titanic',1997,'James Cameron',194,'catastrophic','USA',20,1],
 #     [2,'Spectre',2015,'Sam Mendes',148,'Action','USA/GB',23,1],
  #    [3,'Seksmisja',1983,'Juliusz Machulski',116,'Comedy','Poland',15,1],
   #   [4,'Lord of War',2005,'Andrew Nicol',122,'Drama','France/Germany/USA',21,1]]


import csv,sys

dane=[]
max_lengths=[0,0,0,0,0,0,0,0]
def read_csv(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                row[3]=int(row[3])
                row[0]=int(row[0])
                row[-1] = int(row[-1])
                row[-2] = int(row[-2])
                dane.append(row)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}')
        headers = ['ID', 'Title', 'Director', 'Duration', 'Genre', 'Country', 'Price', 'Amount']
        dane.insert(0, headers)
    return dane

def print_movies():
    how_many_dashes=sum(max_lengths)+9
    print('-' * how_many_dashes)
    for movie in dane:
        x = prepare_column_values(movie)
        print('|{: <{}}|{: <{}}|{: <{}}|{: <{}}|{: <{}}|''{: <{}}|{: <{}}|{: <{}}|'.format(*x))
        print('-' * how_many_dashes)


def max_column_length():
    for movie in dane:
        for i in range(len(movie)):
            if len(str(movie[i])) > max_lengths[i]:
                max_lengths[i]=len(str(movie[i]))
    return max_lengths

def prepare_column_values(movie):
    list_to_format=[]
    for i in range(len(movie)):
        list_to_format.append(movie[i])
        list_to_format.append(max_lengths[i])
    return list_to_format

def search_movies():
    search_string=input('Please enter phrase to search: ')
    for movie in dane[1:]:
        if search_string.lower() in movie[1].lower() or search_string.lower() in movie[-4].lower():
            print(movie)

def rent_movie():
    print_movies()
    choose_movie=input('Please enter movie id to rent: ')
    if not choose_movie.isdigit():
        print("Please enter ID which is an integer/number.")
        return
    for movie in dane:
        if movie[0]==int(choose_movie):
            if movie[-1]>=1:
                print(movie[1],'has been succesfully rented by you.')
                movie[-1]=movie[-1]-1
            else:
                print('This movie is out of stock.')
            return
    print('There is no movie with given id.')

def return_movie():
    returned_movie=input('Please enter id to return: ')
    if not returned_movie.isdigit():
        print('Please enter ID which is an integer/number.')
        return
    for movie in dane:
        if movie[0]==int(returned_movie):
            print(movie[1], 'has been succesfully returned by you.')
            movie[-1] = movie[-1] + 1
            return
    print('There is no movie with given id.')

def write_csv(filename):
    with open(filename, 'w',newline='') as f:
        csvwriter=csv.writer(f)
        for movie in dane[1:]:
            csvwriter.writerow(movie)

def add_movie():
    new_title=input('Please enter title: ')
    new_director = input('Please enter director: ')
    new_duration = int(input('Please enter duration: '))
    new_genre = input('Please enter genre: ')
    new_country = input('Please enter country: ')
    new_price = int(input('Please enter price: '))
    new_amount = int(input('Please enter amount: '))
    new_id=generate_new_id()

    new_movie=[new_id,new_title,new_director,new_duration,new_genre,new_country,new_price,new_amount]
    dane.append(new_movie)

def edit_movie():
    print_movies()
    edit_position = input("Type ID of the movie you want to edit: ")
    if not edit_position.isdigit():
        print('Please enter ID which is an integer/number.')
        return
    for movie in dane:
        if movie[0] == int(edit_position):
            print(movie)
            movie_feature=int(input("Which movie feature would you like to edit? (type feature index): "))
            movie.remove(movie[movie_feature])
            new_feature=input('Type edited value: ')
            movie.insert(movie_feature,new_feature)





def generate_new_id():
    max_id=0
    for movie in dane[1:]:
        if movie[0]>=max_id:
            max_id=movie[0]

    return max_id+1

read_csv('netflix.csv')
max_column_length()

user_regcognition=input('If you are a client type "c". If you are an employee type "e".: ')

is_running=True
while is_running:
    if user_regcognition=='c':
        print('press 1 to list movies')
        print('press 2 to search')
        print('press 3 to rent a movie')
        print('press 4 to return a movie')
        print('press 0 to exit')
    if user_regcognition=='e':
        print('press 1 to list movies')
        print('press 2 to search')
        print('press 3 to rent a movie')
        print('press 4 to return a movie')
        print('press 5 to add a new movie')
        print('press 6 to edit a movie')
        print('press 0 to exit')

    user_response = input()

    if user_response=='1' and (user_regcognition=='c' or user_regcognition=='e'):
        print_movies()
    elif user_response=='2' and (user_regcognition=='c' or user_regcognition=='e'):
        search_movies()
    elif user_response=='3' and (user_regcognition=='c' or user_regcognition=='e'):
        rent_movie()
        write_csv('netflix.csv')
    elif user_response=='4'and (user_regcognition=='c' or user_regcognition=='e'):
        return_movie()
        write_csv('netflix.csv')
    elif user_response=='5' and user_regcognition=='e':
        add_movie()
        write_csv('netflix.csv')
    elif user_response=='6' and user_regcognition=='e':
        edit_movie()
        write_csv('netflix.csv')
    else:
        is_running=False

