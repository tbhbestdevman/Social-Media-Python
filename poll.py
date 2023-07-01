```python
from database import database_connection, PostSchema
from user import current_user

class Poll:
    def __init__(self, question, options):
        self.question = question
        self.options = options
        self.votes = {option: 0 for option in options}

    def vote(self, option):
        if option in self.options:
            self.votes[option] += 1
        else:
            raise ValueError("Invalid option")

    def get_results(self):
        return self.votes

def create_poll(question, options):
    poll = Poll(question, options)
    post = PostSchema(question=question, type='poll', content=poll)
    database_connection.insert(post)
    return poll

def vote_poll(poll_id, option):
    post = database_connection.find_one(PostSchema, id=poll_id)
    if post and post.type == 'poll':
        post.content.vote(option)
        database_connection.update(post)
    else:
        raise ValueError("Invalid poll id")

def get_poll_results(poll_id):
    post = database_connection.find_one(PostSchema, id=poll_id)
    if post and post.type == 'poll':
        return post.content.get_results()
    else:
        raise ValueError("Invalid poll id")
```