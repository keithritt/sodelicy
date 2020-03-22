from ui import UI
from pprint import pprint

#todo - hardcoding my creds for now
#also for now we will assume that a repo has already been created on github
# need to look into storing github creds - either in this script or on server
class Git:
  def __init__(self, domain_code, env):
    #print('Git.__init__({})'.format(domain_code))
    self.domain_code = domain_code
    self.env = env
    # for now we will assume that the domain id and the github repo ID are the same
    # need to check a config first
    self.repo_id = self.domain_code
    self.repo_dir = '/home/ubuntu/'+self.repo_id # hard coding for now - need to get it passed in from run.py

  def run_wizard(self):
    #UI.print('Git.run_wizard()')
    # get repo name
    if not UI.ask_boolean("Is the name of the repo: {}?".format(self.repo_id)):
      self.repo_id = UI.ask("What is the name of the repo?")
    # check if folder is already a repo
    if self.is_git_repo():
      print('this is a git repo')
    else:
      # todo - check to see if thise repo exists on github first
      # note - had errors running this script due to the fact that the directory was not empty
      clone_cmd = 'git clone https://github.com/keithritt/{repo_id}.git {repo_dir}'.format(repo_id=self.repo_id, repo_dir=self.repo_dir)

      output = UI.run(cmd=clone_cmd, cwd='/home/ubuntu/')
      #todo - add logic to parse if response was an error
      print('output = {}'.format(output))

    self.current_branch = self.get_checked_out_branch()
    #print(branch)
    if self.env == 'dev' and self.current_branch != 'dev':
      #print('we need to check out the dev branch')
      if not self.does_branch_exist('dev'):
        self.create_branch('dev')

      self.checkout_branch('dev')

    if not self.is_upstream_set():
      self.set_upstream()

  # runs a command from the repo
  def run(self, cmd):
    print('Now running: {}'.format(cmd))
    return UI.run(cmd, cwd=self.repo_dir)

  def status(self):
    return self.run('git status')

  # check to see if the directory is a git repository
  def is_git_repo(self):
    output = self.status()
    if output[0] == 'fatal: not a git repository (or any of the parent directories): .git':
      return False

    return True

  def get_checked_out_branch(self):
    return self.run('git branch')[0].replace('* ', '')
    #print(output)

  def does_branch_exist(self, branch):
    print('does branch exist')
    local_branches = []
    output = self.run('git branch')

    UI.print_bar()
    for tmp_branch in output:
      tmp_branch = tmp_branch.replace('* ', '')
      if branch == tmp_branch:
        return True

    return False


    print(local_branches)

  def create_branch(self, branch):
    print('create branch ({}) '.format(branch))
    self.run('git branch {}'.format(branch))

  def checkout_branch(self, branch):
    print('checkout branch({})'.format(branch))
    self.run('git checkout {}'.format(branch))

  def is_upstream_set(self):
    print('is_upstream_set()')
    output = self.run('git branch -vv')
    pprint(output)
    for line in output:
      if line == "":
        break
      # ignore branches that dont have the asterisk
      #print(line)
      parts = line.split()
      #pprint(parts)
      if(parts[0] == '*'):

        if '[' in parts:
          return True

        print('before break')
        break #not sure the point of the "Merge" search - skipping until i recall why
        print('after break')
        #find the occurrence of the keyword "Merge" in the output
        print(type(parts))
        pprint(parts)
        merge_idx = parts.index("Merge")
        #print(merge_idx)
        upstream = parts[merge_idx-1];
        if '[' in upstream:
          return True

    return False

  # for now we are assuming that the remote and local names match exactly
  def set_upstream(self):
    print('set_upstream()')
    cmd = 'git push --set-upstream origin {}'.format(self.current_branch)
    print(cmd)
    self.run(cmd)