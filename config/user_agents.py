from fake_useragent import UserAgent

def generate_random_user_agent():
    user_agent = UserAgent()
    return user_agent.random
