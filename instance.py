from github import Github
import constants


class Token:
    g = Github(constants.GITHUB_TOKEN)
    repository_endpoint = constants.REPOSITORY
    repo = g.get_repo(repository_endpoint)
    issues = repo.get_issues(state="open")

    def get_repository(self):
        return self.g.get_repo(self.repository_endpoint)
