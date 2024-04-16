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

hi i'm @basedanarki and here's a hacky update to github2file. no matter what's in your target codebase, if you can access it and your LLM of choice has a context window large enough, you should be able to pull it down and make it useful. we want context/token bloat near zero so make sure you check the txt to delete any crap that makes it in there. (compiled files are weird)

```
python github2frontend.py https://github.com/shadcn-ui/ui

🤔
```

```
python github2fullstack.py https://github.com/PostHog/posthog
```
![WICKED THE TWITCH MEME BTTV EMOJI](https://media.tenor.com/it_JJrYID9wAAAAi/twitch-wicked.gif)

```
github2fullstack.py is at a generically accessible and useful customization point
(add your filetypes, excludes, whatever)
```
