This is mainly for talking to chatbots that have huge context but don't automatically download code from github. 

example use:

```
python github2file.py https://github.com/huggingface/transformers
```

now you can drop transformers.txt into your conversation with Claude, etc.

For a private repository, you can use the following format:
```
python github2file.py https://<USERNAME>:<GITHUB_ACCESS_TOKEN>@github.com/huggingface/transformers
```

(Refactoring your own things!!!🔑)

hi i'm @basedanarki and i refactored this. no matter what's in your target codebase, if you can access it and it's basic xd, you should be able to pull it down and make it useful. we want context bloat near zero so make sure you check the txt to delete any crap that makes it in there. (compiled files are weird)

"""Check if the file is a Python, HTML, CSS, JavaScript, TypeScript, Svelte, or Rust file."""


```
python github2frontend.py https://github.com/shadcn-ui/ui
```

'''generically useful customization point'''
