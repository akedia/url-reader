everyone will quote the GPT-5.4 support.

the more important change is per-topic agent routing.

in Telegram forums, each topic can now bind to a different agent:

channels: {
  telegram: {
    groups: {
      "-1001234567890": {
        topics: {
          "31": { agentId: "starter-support" },
          "30": { agentId: "pro-support" }
        }
      }
    }
  }
}

separate topic, separate session, separate workspace, separate memory.

that's what multi-agent should look like.
one agent, one job. not one agent wearing five masks.