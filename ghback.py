
import requests
import json
from requests.exceptions import RequestException
import logging
import os
import dotenv
import github3

# Initialize logging
# Load environment variables from .env file
dotenv.load_dotenv()
LOGLEVEL = os.getenv('LOGLEVEL', 'INFO').upper()

# Initialize logging
logger = logging.getLogger()
logger.setLevel(LOGLEVEL)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Set logging level to DEBUG to see detailed logs
# log the last 4 characters of the token
logging.info('Starting GitHub backup script...')
logging.info('Fetching starred repositories...')

def fetch_starred_repos():
    """Fetches starred repositories and returns a list of dicts with desired information."""
    starred_repos = []
    try:
        gh = github3.login(token=GITHUB_TOKEN)
        # Fetch starred repositories
        for repo in gh.starred():
            starred_repos.append({
                'name': repo.name,
                'description': repo.description,
                'url': repo.html_url,
                'language': repo.language,
                'stars': repo.stargazers_count,
                'forks': repo.forks_count
            })

    except RequestException as e:
        logging.error(f'Failed to fetch starred repositories: {e}')
    return starred_repos

def backup_starred_repos():
    """Backups starred repositories to a JSON file."""
    repos = fetch_starred_repos()
    if repos:
        with open('starred_repos_backup.json', 'w') as file:
            json.dump(repos, file, indent=4)
        logging.info('Starred repositories backed up successfully.')
    else:
        logging.info('No repositories to backup.')

if __name__ == '__main__':
    backup_starred_repos()