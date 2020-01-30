import sys
import json

def get_role(line):
    line = line.split(',')

    actor_id = line[0]
    movie_id = line[1]
    role = line[2].strip()

    row = {
            'movie_id': movie_id,
            'role': role
        }
    return [actor_id, row]

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
    return row

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
                row = get_actor(line)
                memory.append(row)
            else:
                actor_id, role = get_role(line)
                if actor_id not in memory:
                    memory[actor_id] = []
                    memory[actor_id].append(role)
                else:
                    memory[actor_id].append(role)
        except:
            error += 1

    fileHandler.close()
    print('count', count)
    print('error', error)
    return memory

if __name__ == "__main__":
    actors = []
    actors = read_csv(actors, 'actors.csv')
    roles = {}
    roles = read_csv(roles, 'roles.csv')
    print(len(roles))
    print(len(actors))
    with open("actor_with_role.json", "a") as write_file:
        for actor in actors:
            actor_id = actor['actor_id']

            if actor_id in roles:
                actor['roles'] = roles[actor_id]
            else:
                actor['roles'] = []
            json.dump(actor, write_file)
            #print(actor)