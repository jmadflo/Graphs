import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.reset_graph
    
    def reset_graph(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset_graph()
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User #{i}")

        # Create friendships
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                if user_id != friend_id: # avoid being friends with oneself
                    possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships) # randomize position of each possible friendship within the list

        # add the first (num_users * avg_friendships // 2) possible friendships from our shuffled list to the social graph
        for i in range(num_users * avg_friendships // 2):
            self.add_friendship(possible_friendships[i][0], possible_friendships[i][1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = [[user_id]]
        while len(queue) > 0:
            path = queue.pop(0)
            num = path[-1]
            # add new entry to visited with the path if its not already there
            if num not in visited:
                visited[num] = path
                # add each friend of this user to the path and add each new path to the queue
                for friend in self.friendships[num]:
                    new_path = list(path)
                    new_path.append(friend)
                    queue.append(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
