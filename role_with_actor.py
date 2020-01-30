import sys
import json

def get_role(line):
    line = line.split(',')
   
    actor_id = line[0]
    movie_id = line[1]
    role = line[2].strip()

    row = {
        'actor_id': actor_id,
        'movie_id': movie_id,
        'role': role
    }
    return row

def get_actor(line):
    line = line.split(',')

    actor_id = line[0]
    firstname = line[1]
    lastname = line[2]
    gender = line[3].strip()

    row = {
        'actor_id': actor_id,
        'firstname': firstname,
        'lastname': lastname,
        'gender': gender
    }
    return [actor_id, row]

def read_csv(memory, csvfile):
    count = 0
    error = 0

    fileHandler = open(csvfile, "r", encoding="utf-8")
    while True:
        try:
            count += 1
            line = fileHandler.readline()
            line = line.encode('ascii', 'ignore').decode('ascii')
            if not line: break

            if type(memory) is list:
                row = get_role(line)
                memory.append(row)
            else:
                actor_id, row = get_actor(line)
                memory[actor_id] = row
        except:
            error += 1

    fileHandler.close()
    print('count', count)
    print('error', error)
    return memory

if __name__ == "__main__":

    roles = []
    roles = read_csv(roles, 'roles.csv')
    actors = {}  
    actors = read_csv(actors, 'actors.csv')
    print(len(roles))
    print(len(actors))
    count_of_no_actors = 0
    with open("data_file.json", "a") as write_file:
        for role in roles:
            role_actor_id = role['actor_id']
            
            if role_actor_id in actors:
                actor_info = {}

                actor_info = actors[role_actor_id]
                role['actor'] = actor_info
                del role['actor_id']
                json.dump(role, write_file)

                
            else:
                count_of_no_actors +=1
            # output of the program to be sent to file
            # python insertData.py > output.txt
    print(count_of_no_actors)      