def commit_callback(commit):
    if commit.author_email == b'sasheenwidanagamage@gmail.com':
        commit.author_email = b'chamodikumarage2003@gmail.com'
        commit.author_name = b'chamodi-kumarage'
    if commit.committer_email == b'sasheenwidanagamage@gmail.com':
        commit.committer_email = b'chamodikumarage2003@gmail.com'
        commit.committer_name = b'chamodi-kumarage'
