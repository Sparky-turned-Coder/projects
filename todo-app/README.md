# First project: A TODO GUI application

#### First lesson:
    
    Buttons don't store data. Buttons trigger functions (behavior).
    Functions then <em>decide</em> what data to create or modify.
    
##### Note: The button click must call a function.

#### That function can:
    
    - Add "New Task" to your list[ ]
    - Update the GUI
    - Print something
    - Do anything you want

#### Mental Walkthrough
<ol>
<li>App starts</li>

<li>tasks = [ ] exists</li>

<li>Button is on screen</li>

<li>User clicks Add Task</li>

<li>Tkinter says:</li>
        
        “Hey Python, run this function”

<li>That function:</li>
        
        adds "New Task" to tasks
        tells the list widget to show it
</ol>

What should the task function need acces to?

The "Task" function needs access to:

1. A running list stored in memory
2. The button, as clicking it will trigger the function
3. The GUI so that it can respond to the user with some kind of output

So, now we know what we need first:  <strong>A Function</strong>
    
    Functions don't magically "see" everything.
    They can only see:

<ul>
<li>variables in their scope</li>
<li>or things passed to them</li>
</ul>

So we must <em>design</em> things so the function can see:

    - the "tasks" list
    - the GUI list widget

### NOTE: Big concept

<strong>Code:</strong>

    tasks = []

    def add_task():
        # 1. Update the data
        tasks.append("New Task")

        # 2. Update the GUI
        task_listbox.insert(tk.END, "New Task") 

Right now we have two sources of truth:
    
    - tasks >> the real data saved in memory
    - Listbox >> a visual <em>copy</em> of that data

Whenever you update one without the other, things go adrift.

So the <em>desgin</em> goal becomes:

    One source of truth, one way to render it.

Bottom line, 'tasks' should be the boss. Listbox is simply a visual copy of that data.

#### The GUI should:

    - never own data
    - only render data
    - only request changes to data

That mental model scales from tiny Tkinter apps all the way to massive web systems.

Excerpt from conversation with Chat Gippity:
    
    Chris:
    It makes sense that the GUI should remain a visual representation of the actual, hard-coded data.  But when I first thought about it, my inclination was to say the GUI anyway. I reasoned that this would give the User the most control, that if the data and GUI are out of sync, it stand to reason giving the user the power to fix things.

    But I can also see why that might not be such a good idea. The data is the important bit.  If it's lost accidentally, it's lost forever, say if the User makes a mistake because I went and gave them TO MUCH power.  In that regard, leaving the GUI as essentially a visual copy of the raw data makes a lot more sense. 

    So, the data should be the boss. Dictating everything the User sends, recieves, and can see on the screen.

    As for the bonus thinking ... I would think that you would need to rewrite it so that 'tasks' itself updates the listbox.  I've never done it, but it sounds the most reasonable idea to me.

    Gippity:
    👏 That reasoning is excellent. You just articulated, in plain English, one of the oldest and most important ideas in software design:

        Data is the source of truth.
        The UI is a controlled window into that data.

    Your instinct about “giving the user power” is thoughtful—but you caught the key trade-off yourself:

        power without guardrails = accidental data loss.

    That’s a professional-level insight, not beginner stuff.


#### So, a tiny refactor, because:
Right now, my function does <em>two</em> things:

    1. Changes the data
    2. Changes the GUI directly

We're going to split responsibilities.

#### New Rule:
Only <em>one</em> function is allow to touch the Listbox directly.

That function's job:

    - Clear the Listbox
    - Rebuild it from 'tasks'

Let's call it (conceptually for now):

    refresh_tasks()



