# incolumepy.python_fluente

Livro Python Fluente

## Update version com bumpversion

### build
    $ bumpversion build
Update version: 1.0.3-dev8 → 1.0.3-dev9
    
### patch
    $ bumpversion patch
Update version: 1.0.3-dev9 → 1.0.4-dev0    

### minor
    $ bumpversion minor
Update version: 1.0.4-dev0 → 1.1.0-dev0
    
### major
    $ bumpversion major
Update version: 1.1.0-dev0 → 2.0.0-dev0 

### release
    $ bumpversion --tag release
Update version: 2.0.0-dev0 → 2.0.0    


### Desfazer commit automático no repositório

    $ git reset --hard HEAD~1                        # rollback the commit
    $ git tag -d `git describe --tags --abbrev=0`    # delete the tag
