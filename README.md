# pycord-autocomplete-error

- Install PyCord, `pip install py-cord`
- Edit the bot.py file and add your token.
- Run the bot.
- Client uses the `/hello` command and the `option` field attempts to autocomplete with a simple static list.


Error:

```
Task exception was never retrieved
future: <Task finished name='Task-17' coro=<ApplicationCommandMixin.on_application_command_auto_complete.<locals>.callback() done, defined at /home/fuz/.local/lib/python3.8/site-packages/discord/bot.py:827> exception=HTTPException('400 Bad Request (error code: 50035): Invalid Form Body\nIn data: Field "_choices_type" is required to determine the model type.')>
Traceback (most recent call last):
  File "/home/fuz/.local/lib/python3.8/site-packages/discord/bot.py", line 830, in callback
    return await command.invoke_autocomplete_callback(ctx)
  File "/home/fuz/.local/lib/python3.8/site-packages/discord/commands/core.py", line 1003, in invoke_autocomplete_callback
    return await ctx.interaction.response.send_autocomplete_result(
  File "/home/fuz/.local/lib/python3.8/site-packages/discord/interactions.py", line 1017, in send_autocomplete_result
    await self._locked_response(
  File "/home/fuz/.local/lib/python3.8/site-packages/discord/interactions.py", line 1090, in _locked_response
    await coro
  File "/home/fuz/.local/lib/python3.8/site-packages/discord/webhook/async_.py", line 215, in request
    raise HTTPException(response, data)
discord.errors.HTTPException: 400 Bad Request (error code: 50035): Invalid Form Body
In data: Field "_choices_type" is required to determine the model type.
```
