#!/usr/bin/python3

def load():
  envs = {}

  with open('.env') as f:
    lines = [line.rstrip() for line in f]

  for line in lines:
    env = line.split('=')
    envs[env[0]] = env[1]

  return envs

if __name__ == "__main__":
  print(load())