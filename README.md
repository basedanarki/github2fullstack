## (7/26/24) just use [code2prompt](https://github.com/raphaelmansuy/code2prompt/) it's so much better, dude. jeeesh it's great. 

### copy/paste the code2prompt readme to your sota coder llm with your codebase context and it'll compose an ideal terminal command for you --don't let it use gitignore just don't, be literal, you're welcome. 

#### tell it what you don't need, or code it yourself '--exclude stuff'

#### these single-file codebases as md files are the best thing ever to include in Claude projects, @file link to continue dot dev, whatever.

#### yeah i'm wrecking this readme but trust me on the value here ok this one, is huge

#### you can use the 'generate readme' template to standardize readmes across ALL codebases you use. mess with the template if you want.

#### i love this, and use it to standardize the libraries i want to understand quickly myself to be understood for nuanced implementation by claude

#### [-Anarki](https://x.com/basedanarki)

#### p.s. [continue dot dev](https://github.com/continuedev/continue) > github copilot. testing [Aider](https://github.com/paul-gauthier/aider) a little later today for core workflow adoption: agentic pair programming. LFG!

#### alright here's my old irrelevant garbage for posterity:
--- 


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
