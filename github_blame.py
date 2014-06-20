import webbrowser
try:
    from .github import GithubWindowCommand, with_repo
except ValueError:
    from github import GithubWindowCommand, with_repo


class GithubBlameCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        webbrowser.open_new_tab(repo.blame_file_url(
            self.relative_filename(), self.line_number()))
