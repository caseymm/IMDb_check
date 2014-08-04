import requests
import json

def get_info(actor):
    get_all = "name="+actor+"&format=JSON&filmography=1&limit=1&uniqueName=1"
    actor_info = requests.get('http://www.myapifilms.com/imdb?', params=get_all)
    
    my_json = actor_info.json()
    
    for obj in my_json:
        dict = obj
        for entry in dict:
            all_film_types = dict['filmographies']
    
    #print all_film_types
    
    for role_type in all_film_types:
        section = role_type['section']
        #print section
        if section == 'Actor' or 'Actress':
            filmography = role_type['filmography']
            print
            print actor + ' acted in:'
            #print filmography
            for film in filmography:
                IMDBid = film['IMDBId']
                year = film['year']
                title = film['title']
                print year, title, IMDBid
            
            return filmography
        
def compare_actors(actor_a, actor_b):
    actor_a_dict = get_info(actor_a)
    actor_b_dict = get_info(actor_b)
    
    print
    print actor_a + ' and ' + actor_b + ' both appeared in:'
    
    count_films = 0
    for film in actor_a_dict:
        if film in actor_b_dict:
            count_films += 1
            IMDBid = film['IMDBId']
            year = film['year']
            title = film['title']
            print year, title, IMDBid
    
    if count_films < 1:
        print "  These actors haven't appeared in anything together yet!"

print "Please enter the names of two actors to see what, if ever,\
they have starred in together."

actor_a = raw_input ("Enter the name of the first actor: ")
actor_b = raw_input ("Enter the name of the second actor: ")
compare_actors(actor_a, actor_b)