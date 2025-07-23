# Importing Initial Data
Once you’ve got Tabbycat installed, the next step is to import data for the tournament: that is, import details of teams, speakers, adjudicators and rounds. There are a few ways to do this, each with their advantages and disadvantages.

## Demonstration data
If you’re just learning or experimenting with Tabbycat, there are two demonstration datasets available, each with a sample set of teams, adjudicators, etc., so that you can immediately start running rounds. Just be aware that these probably won’t relate to anyone at your real-life tournament.

To load a demonstration dataset, click New Tournament link on the home page (once logged in as admin). You’ll see a page titled “Create New Tournament”. Scroll to the bottom of this page and click on one of the links at the bottom.

## Simple importer
The simple importer is the easiest way to get a tournament going, and we recommend it for small- and medium-sized tournaments. It allows you to add institutions, teams, adjudicators, venues, venue categories and venue constraints. (If you need to add anything else, use the Edit Database area instead.)

To get started, create a new tournament using the New Tournament link on the home page (once logged in as admin). It’ll ask you for a few basic pieces of information.

Then, once you’re in your tournament, click Setup in the left-hand menu, then Import Data, to open the simple importer.

You first need to add institutions. Once institutions are added, you can then add teams and adjudicators in the relevant sections. Each of these is a two-step process:

- For institutions and venues, it will first ask you to copy-paste a list of names and properties in a comma-separated table format. The second step is to confirm individual fiels.

- For teams and adjudicators, it will first ask you how many teams/adjudicators to add for each institution (or who lack an institutional affiliation). The second step is to fill in their details, for example, names.

Finally, if you would like to use venue categories and/or venue constraints, you can do so using the two last sections of the simple importer.

## Editing the database
Sometimes, the simple importer just isn’t enough—whether because you need more customization than the simple importer handles (e.g. adjudicator feedback questions), or because some participants changed their details after you imported the inital data. In this case, the easiest thing to do is to edit the database via the Django administrative interface (under Setup > Edit Database).

The general pattern goes like this: Go to Setup > Edit Database, find the type of object you wish to add/change, and click “Add” or “Change”. Then, fill in what you need to and save the object.

# Starting a Tournament

This page outlines a few things you should do at the start of a tournament, after you’ve imported the initial data. Once you’ve done these, proceed to running a tournament.

## Tournament configuration

After importing all your data you can log into the site as an administrator by loading up the homepage and then using the Login button in the lower-right. From there you should go to the administration section of your tournament, and then go to the tournament configuration page by clicking Setup then Configuration in the menu.

Here you can adjust the debate rules and interface options to your liking then hit Save when finished. We also offer a number of presets that apply particular rule sets (such as the Australs rules) or feature sets (such as displaying information normally released during briefs on the website).

## Special data types and options

There are a few optional fields that are not covered in the initial data templates, in the visual importer, or that may only be relevant in particular scenarios. It’s worth going over these quickly to see if they are needed for your tournament. You can view and edit these fields in the Edit Database area (link is in the menu under the tournament’s name).

Adjudicator Feedback > Adj Feedback Questions
- As described in Adjudicator Feedback, the types of questions that can be posed for adjudicator feedback are able to be heavily customised. If you are customising your feedback form it should be done here, and before the tournament starts.

- Authentication and Authorisation > Users
Here you can add new admin users (those with full access) as well as new assistant users those (who can only do common data-entry tasks but not edit or view the full tab interface). See User Accounts for information on how to do this.

Participants > Regions
- Optionally, each institution may belong to a Region. An institution’s region is used    within the adjudicator allocation process to visually identify teams and adjudicators for the purposes of highlighting diversity issues. These have traditionally been used for geographic regions (such as Oceania), although could be repurposed as arbitrary markers of information — for example they could be used to denote teams from a particular State, institutional size, or circuit.

Participants > Adjudicators
- An adjudicators Base Score represents their relative ability to judge important rooms, where adjudicators with higher numbers will, relative to the other adjudicators, be placed in better roles (ie as Chairs) and in the rooms you deem most important in each round. If you are running a small tournament, and plan to do your allocations manually, you can set everyone’s number to the same amount.

- For larger tournaments, particularly those that collect feedback, see the Adjudicator Feedback section for more information on how base scores and other variables influence the automated allocation process.

- Regardless of how you score the adjs, if you have changed the minimum chairing score in settings, you’ll want to make sure there are enough adjudicators that meet this minimum threshold or the automated allocator may not function effectively.

- All types of conflicts are assigned to the relevant adjudicator. Adjudicators can be conflicted against particular teams, particular institutions, and other adjudicators. Each of these is a located in a tab at the top of the page.

- Each adjudicator’s gender is optional and is not displayed publicly; it is only shown in the adjudicator allocation interface

- Each adjudicator’s pronoun is optional, and is only displayed if you use Tabbycat to print the ballots and feedback sheets for each round.

Participants > Teams
- Note the distinction here between full name and short name. The latter is used on pages where space is tight, such as the draw displays or the adjudicator allocation interface.

- Note that “Uses institutional prefix” option. With this option on, a team from the ‘MUDS’ institution named ‘1’ or ‘Gold’ would be displayed as ‘MUDS 1’ or ‘MUDS Gold’.

- At present, setting a team’s type to Bye, Swing, or Composite only affects very particular circumstances, and should be considered unnecessary.

- If you do have composite teams, and wish to have them be conflicted by adjudicators from each respective instutution, you’ll need to add a new team conflict to each adjudicator from each institution.

- If you do have swing teams, or teams that are otherwise ineligible for breaking, this is typically handled through the breaks interface in the main site.

Participants > Speakers
- Each speaker’s gender is optional and is not displayed publicly; it is only shown in the adjudicator allocation interface.

- Each speaker’s pronoun is optional, and is only displayed if you use Tabbycat to print the ballots and feedback sheets for each round.

Venues > Venues
- A venue’s priority determines its priority in being allocated. If there are 20 debates, and 30 rooms, the 20 rooms with the highest priorities will be chosen. Furthermore, if particular debates are marked as important during the draw process, those debates will receive the rooms with the highest priorities. In this way you can give close rooms to members of the adj core, or give larger rooms to debates that will draw a large audience.

Venues > Venue Categories
- Venue categories are not needed for most kinds of tournaments. Their purpose is to classify particular venues, such as venues all within one building or venues that are accessible. Once assigned these categories can display in the venue’s name — ie “Red 01.01” or be used to assign Venue Constraints that match particular teams, institutions, or adjudicators to particular types of venues.

# Running a Tournament

Once you’ve finished the steps in Starting a Tournament, you’re ready to go! This page outlines what you would do for each round during the tournament. After the tournament, proceed to Finishing a Tournament.

This is all done from the admin area (i.e., by the tab director or adjudication core member). In the admin area, tournament-wide pages (feedback, standings, and break) are at the top of the left-hand menu, while round-specific pages (availability, draw, display, motions, and results) are in dropdown’s organised by each round’s abbreviation.

The basic workflow for each round is:

1. Mark the teams, adjudicators, and venues present as available
2. Generate the draw and allocate the adjudicators
3. Show/release the draw
4. Release/enter the motions
5. Have the debates
6. Enter results
7. Advance to the next round

## Availability
Set availability. For each round, you need to set the venue, team and adjudicator availability. If any of those are not marked as available they will not be used within the draw; so this feature is mostly useful for when adjudicators or venues are only available for certain rounds.

To do this, click the round in the menu, then click Availability. Here you can then go to the availability pages for venue, teams, and adjudicators, or check in everything at once. When you’ve set everything appropriately use the Generate Draw button in the top right to advance.

## Generating the draw
1. Confirm the draft draw. After advancing from availability section you will first be shown a draft draw that details how the draw was formulated, pointing out pull-ups and conflict swaps and the like.
2. Once on the confirmed draw page you can click Allocate Adjudicators.
3. Allocate the adjudicators. Changes here will auto-save; feel free to return to the Draw when needed. See adjudicator allocation for more details about the allocation process.

## Releasing the draw
Once you’re happy with your adjudicator allocation, you’re ready to start the round.

1. Release to general assembly. From the Display page for that round, go to Display Draw ordered by Room or Display Draw ordered by Team (whichever you prefer). Then put it up on the projector. There are automatic scroll buttons and buttons for changing text sizing.
2. Release to public. If you’re using the public draw function (where the draw is posted publicly to your Tabbycat website) use the Release to Public button to allow the page to display.

## Entering and Releasing Motions
Tabbycat is agnostic as to whether you enter motions into Tabbycat before or after they are shown publicly. However, they must be entered at some point before ballots are entered.

1. Enter the motion text. Either before or after their public release motions can be entered in the Motions section for that round.
2. Release to general assembly. If you are entering motions before they are publicly revealed note that there is a Display Motions button in the Display area that allows you to do a Power Point style motion release.
3. Release to public. As with draws, if you have the enable public view of motions setting configured your Tabbycat website will display a running list of motions from the tournament. When this is on, using the Release Motions to Public button on the Motions page will mark the current set of motions as able to be displayed on this page.

## Entering Results
1. Enter debate results and feedback as they come in (and/or allow online entry of results and feedback).
2. Both results and feedback entered in the tab room or online need to be confirmed before the results are counted. To confirm a debate ballot and the debate as a whole, the confirmed checkbox under Ballot Status should be ticket in addition to the Debate Status being set to Confirmed.
3. Note that you can track data entry progress from the Overview page for the tournament.

## Advancing to the next round
Once you’ve got all the results entered and confirmed, you’re ready to progress to the next round. This can be done by going to the Results area, and then using the Complete Round button.
Warning
- When you advance to the next round, if you’ve enabled public results, the results for the current round (which is now the previous round) will be released to the public unless the round is marked as “silent” in the database. So if you’re careful about when results should be released, don’t change the current round until you’re ready to release those results.

Note
- There is a design assumption that you will always want to release results for non-silent rounds before you start working on the draw for the next round. If this isn’t true for you, please get in touch with us so that we know. The workaround is to make all rounds silent, then unsilent them when you’re ready to release results.

# Finishing a Tournament
This page outlines some final steps to take after the conclusion of outrounds.

## Tab Release
Tabs can be released under Setup > Configuration > Tab Release. Tabbycat offers the following system tabs:
- Team Tab
- Speakers Tab
- Replies Tab
- Motions Tab

You can configure the team, speakers and replies tab to display only a certain number of speakers, e.g., to show only a “Top 10 Speakers” tab.

If you defined any speaker categories (for example, Novice, ESL or EFL), a tab for each category marked “public” can also be released using the Release speaker category tabs to public. You can similarly limit each of these tabs to display just the top few speakers, in the definition of the speaker categories. The speaker categories not marked public are not released by this option.

You can also redact individual speaker’s identifying details (name, team, and institution) from the public individual tabs. You can do so by going into the Edit Database area, going to Participants > Speakers, finding the speaker and clicking the Anonymous box (and saving).

Silent and non-completed rounds aren’t released unless the Release all round results to public option is checked, so once your tournament has concluded, you probably want to change this setting.

## Wrapping Up
You probably want to turn off the Public ballots, Public feedback, Feedback progress, and Public draw features under Configuration at this stage as they no longer have any use.

# Feature Notes
## Adjudicator Feedback
You can set the questions that are used on adjudicator feedback forms. The only field that is permanently there is the score field, which is an overall score assessing the adjudicator. All other questions (including a generic comments section) must be defined if you want them to be on the form.

Currently, there are two methods of setting questions:
- Through the edit database area. Go to Setup > Edit Database, then click Change next to Adjudicator feedback questions. You can add questions here.
- Using the importtournament command.

Most of what you need to know is explained in help text in the edit database area. (Even if you’re using importtournament, you might find the field descriptions in the edit database area helpful.) Some more details are here.

### Answer types and options
Type
- checkbox
- yes/no dropdown
- integer textbox list of numbers (min_value, max_value)
- integer scale with circle options (min_value, max_value)
- float list of numbers (min_value, max_value)
- text
- long text
- select one (choices)
- select multiple (choices)

Options:
- min_value and max_value specify the minimum and maximum allowable values in the field. Mandatory for “integer scale” types and optional for “integer (textbox)” and “float” types.
- choices is used with “select one” and “select multiple” types, and is a comma-delimited list of possible answers, e.g. biased,clear,concise,rambly,attentive,inattentive
- required specifies whether users must fill out the field before clicking “submit”. This requirement is only enforced on public submission forms. It is not enforced on forms entered by tab room assistants.

The exception to this is the “checkbox” type. For checkboxes, “required” means that the user cannot submit the form unless the box is checked. Think of it like an “I agree to the terms” checkbox. This isn’t a deliberate design decision—it’s just a quirk of how checkboxes work on web forms.

### Different questionnaries
Tabbycat allows you to specify two questionnaires: one for feedback submitted by teams, and one for feedback submitted by adjudicators. You must specify in each question whether to include the question in each questionnaire.
- from_team, if checked, includes the question in feedback submitted by teams
- from_adj, if checked, includes the question in feedback submitted by adjudicators

### Who gives feedback on whom?
Tabbycat allows for three choices for which adjudicators give feedback on which other adjudicators:

- Chairs give feedback on panellists and trainees
- Chairs give feedback on panellists and trainees, and panellists give feedback on chairs
- All adjudicators, including trainees, give feedback on all other adjudicators they have adjudicated with

You can set this in the feedback paths option under Setup > Configuration > Feedback. Your choice affects each of the following:
- The options presented to adjudicators in the online feedback form
- The printable feedback forms
- The submissions expected when calculating feedback progress and highlighting missing feedback

The feedback paths option only affects feedback from adjudicators. Teams are always assumed to give feedback on the orallist, and they are encouraged to do so through hints on the online and printable feedback forms, but there is nothing technically preventing them from submitting feedback from any adjudicator on their panel.

### How is an adjudicator’s score determined?
For the purpose of the automated allocation, an adjudicator’s overall score is a function of their base score, the current round’s feedback weight, and their average feedback score. This number is calculated according to the following formula:

\textrm{score} = (1-w)\times\textrm{base score} + w\times\textrm{average feedback score}
score = (! - w) x base score + w x average feedback score

where w is the feedback weight for the round. Note that because the feedback score is averaged across all pieces of feedback (rather than on a per-round total) rounds in which a person receives feedback from many sources (say from all teams and all panellists) could impact their average score much more than a round in which they only receive feedback from one or two sources.

Under this formula, each round’s feedback weight can be used to determine the relative influence of the base score vs feedback in determining the overall score. As an example, say that an adjudicator received 5.0 as their base score, but their average feedback rating has thus far been 2.0. If the current rounds’ feedback weight is set to 0.75, then their overall score would be 2.75. If the current round’s feedback weight is set to 0.5 their score would be 3.5. If the weight was 0, their score will always be their base score; if the weight was 1 it will always be their average feedback value.

Note
- To change the weight of a round you will need to go to the Edit Database area, open the round in question, and change its Feedback weight value. It is common to set rounds with a low feedback weight value early on in the tournament (when feedback is scant) and to increase the feedback weight as the tournament progresses.

Note
- A participant’s base score can, in conjunction with feedback weight, also be used as a manual override for an adjudicator’s overall ranking. At several tournaments, adjudication cores have set every round’s feedback weight to 0, and manually adjusted an adjudicator’s base score in response to feedback they have received and reviewed. In this way complete control over every adjudicator’s overall score can be exerted.

Note
- If feedback from trainee adjudicators is enabled, any scores that they submit in their feedback are not counted towards that adjudicator’s overall score.

### Ignoring/Discarding feedback
There are some cases where feedback should be discarded or ignored, but there are some differences between the two. Discarded feedback is mostly due to having another piece of feedback that supersedes the discarded ones. Ignored feedback is different as it still counts the affected feedback as submitted, just inconsequential, ignored in the adjudicator’s score calculation.

Feedback can be marked as discarded in the database view, under the confirmed field. It can also be marked as ignored in the same view. Controls to reverse these designations are also available there. To mark feedback as ignored, an option is available in the administrator’s and assistant’s feedback adding form, as well in the form of a toggle link at the bottom of each card.

## Adjudicator allocation
The adjudicator allocation screen offers the ability to automatically generate an allocation and/or allow you to create or edit an allocation manually. This interface is somewhat complex as it attempts to provide all of the information needed to inform allocation while also providing a number of automatic and manual tools for the allocation process itself.

### Assigning Debate Priority
For tournaments with more than a few debates you generally want to begin the allocation process by applying a priority value to your debates. A debate’s priority value is used by the automatic adjudicator allocator (or the preformed panel indicator) to match the strongest panels to the debates that need them most.

The prioritise button in the top-left allows you to assign a priority value automatically based on a debate’s bracket or its ‘liveness’. Remember that in early rounds there are usually not enough results for the liveness of each debate to be distinct and that Tabbycat measures liveness based on the sum of all live break categories — a debate can have more liveness points than it has teams if there are teams that are live in multiple categories.

Note
- The automatic prioritiser never uses the ‘highest’ priority value so that you can easily use this to highlight the debates that need the strongest panels without needing to redistribute the priority of other debates.

Regardless of whether you automatically assign priority, there are sliders to the left of each team that can be used to manually specify priority. These are usually used to override the automatic priority of a debate if that matchup needs and especially strong/weak/mediocre panel for reasons that are not reflected in its bracket/liveness.

Note
- If each debate’s priority is the same, the automatic adjudicator will fall-back on using the debate’s bracket as a substitute for priority. Thus, you can skip the prioritisation process (or only prioritise the most/least important debates) if you want a relatively even spread of panellists (e.g. during Round 1).

### Automatic Adjudicator Allocation
Once you are happy with your priorities you can begin assigning adjudicators. This also has an (optional) automatic process that will create panels for you. In creating these panels automatically, the allocator will:
- Avoid creating ‘hard’ conflicts (i.e. personal or institutional clashes) between adjudicators and teams while also trying to avoid ‘soft’ conflicts (i.e. avoiding an adjudicator seeing the same team again).
- Form panels whose relative average voting score matches the relative priority you assigned to each debate.
- Allocate trainees (unless disabled or none are under the threshold) to panels (allocated first to the highest-strength panels).
- Violate the above intents in cases where there are inescapable constraints — e.g. if there are too many soft or hard conflicts to avoid creating panels that do not trigger them.

Note
- Remember that Tabbycat will only automatically allocate adjudicators that have been marked as available for this round.

To begin this process, click the Allocate button in the top-left. If you have formed preformed panels for this round, the modal will first ask whether you want to assign adjudicators using those panels; otherwise the modal will contain a number of options that can be used to control the allocation. In general, the minimum feedback score value is the most important setting to consider as it determines the threshold needed for adjudicators to not be allocated as trainees.

Once you click Auto-Allocate Adjudicators the modal should disappear and your panels should appear. At large tournaments, and in the later rounds, it is not unheard of for this process to take a minute or longer.

Note
- You can re-run the automatic allocation process on top of an existing allocation. Thus it is worth tweaking your priorities or allocation settings if the allocation does not seem optimal to you. Also note that the allocation process is not deterministic — if you rerun it the panels will be different.

Once your adjudicators have been allocated you can drag and drop them on to different panels. You can also drag and drop them to the ‘unused area’ (the gray bar at the bottom of the page) if you wish to store them temporarily or remove them from the draw. Dropping an adjudicator into the chair position will ‘swap’ that adjudicator into the previous position of the new chair.

### Saving, Live Updates, and Sharing
Changes to your panels save automatically and you can exit the allocation page whenever you wish.

In addition, the allocation pages maintain a ‘live’ connection to the server that shows updates made by other users who are viewing/using the same page. That is to say, if two people on two computers are both viewing the allocation page they should see each other’s changes in real-time. This allows you to ‘distribute’ the task of allocation across individual people (rather than sharing a screen/projector) if desired.

Note
- It is possible to have users ‘undo’ or ‘overwrite’ each others changes despite this live system, e.g. if both users drag and adjudicator somewhere at the same time.

If you are dividing the task of allocation across multiple people, the Sharding system can help by allowing individuals to limit their view of the draw. The use case here is usually to divide the draw up into mutually-exclusive subsets so that individuals (or groups) of the adjudication core can focus on creating panels across the draw in parallel.

To activate sharding, click the small icon to the right of the “Allocate” button. This then presents a number of options for how the draw is divide up into distinct sets. If you want to ensure that each person opens a completely distinct set of the draw, you will need to coordinate the options that each user selects here. They will need to set the same options for Shard Mix, Shard Split and Shard Sort but select a different Open option (i.e. opt-in to viewing a different shard from the other users). The ability to exit a sharded view is available in the same dialogue.

### In-Place Highlights
Adjudicators and teams may have borders of varying colors. These borders indicate that there is a clash — soft or hard — within a debate and highlights the teams/adjudicators that have triggered this. There is a key for these colors available at the top of the page — e.g. orange means institutional conflict while blue means this adjudicator has seen this adjudicator/team before.

In general, you want to be on the lookout for red borders (‘hard conflicts’) and for teams with orange borders (institutional conflicts). Blue borders on teams/adjudicators and orange borders between adjudicators are usually of lesser concern.

Note
- There are two ‘special’ types of highlight — a gray background in the chair position (no chair) or in the panellist position (the panel is not an odd-size). Adjudicators may also have a black background if they have not been marked as available.

### Hover Highlights
When you hover over an adjudicator or team, they will take on a purple background and other adjudicators or teams may suddenly have different colored backgrounds. These indicate the conflicts that this team/adjudicator has with those other teams/adjudicators. By showing this information you can avoid swapping that adjudicator into a new debate which they have a conflict with.

When you hover over an adjudicator or team the top-most area of the screen will show additional information about them, such as all of their previous institutions, their conflicts, their break category, their team members, their region, and who they saw in the last few rounds.

### Toggle Highlights
In the top-right of the interface are a number of toggles that changes the color of adjudicators and teams to more easily check specific types of information. For example, selecting the gender toggle will color-code teams and adjudicators with the gender that has been recorded in Tabbycat. Note that when a toggle is active, the color key will update to show the meaning of these new colors.

Note
- When finalising an adjudication you may want to ensure you have turned off any toggle highlights — often they make it more difficult to see the border colors that indicate conflicts.

## Breaks and Break Rounds
In Tabbycat, elimination rounds (sometimes called outrounds or the final series) are called “break rounds”, and the qualification of teams to compete in the elimination phase of a tournament is called the “break”.

### About break categories
Tabbycat supports multiple and arbitrarily-named break categories. Most tournaments will have just one category, typically called “Open”, leading to the grand final. Some tournaments also have restricted-eligibility break categories, for example, for novice teams or teams for whom English is a second language.

Having multiple break categories is intended for tournaments where multiple parallel elimination phases derive from the same preliminary rounds (inrounds). It’s not for parallel but distinct competitions—for those, you should create distinct tournaments.

### Break qualitifcations rules 

Tabbycat supports several break qualification rules, and each break category must be configured to use one of them. Most tournaments will use “Standard”, which is the default.

Standard: The top n teams break. This is the default, and most tournaments use this rule.

There are more but this is the one that we are going to use in alegator

Note
- The break generators are somewhat more complex than described in the above table: among other things, they also handle cases where there is a tie for the last place in the break, and for those break categories marked “general”, they will show where ineligible teams would have broken, had they been eligible.

### Setting up break categories and rounds
For each break category in your tournament, you need to do two things:

- Create (and name) a break category
- Set the eligibility of teams to compete in the category

If you only have one break category (open) and you create your tournament using the “Create New Tournament” page, simply enter the number of teams in the break (e.g., 8 if you’re breaking to quarterfinals). Tabbycat will create the break category and break rounds for you. For any further break categories, you’ll need to go to the Breaks item in the left-hand menu for a particular tournament and then click Break Categories. Fill out the forms for the number of new break categories and save. Rounds will be created automatically. You’ll still need to set the eligibility of teams though, as in (3) below.

If you create your tournament using the importtournament command or in Edit Database, you’ll need to do all three steps above yourself. You may also want to edit the break rounds (2) to change their names.

1. Creating break categories
If using the importtournament command, there is an example file, break_categories.csv, that you can copy and adjust. If using Edit Database, add categories under Break Qualification > Break categories.

Most of the fields are self-explanatory or described on the Edit Database form, except for one: “rule”, which sets the break qualification rule. Permissible values are described in Break qualification rules above. If using importtournament, be sure to use the correct string (in brackets in the table). The rule defaults to “Standard” (standard).

Note
- The “institution cap” field was removed in Tabbycat 1.0. All Australs break qualification rules are now hard-coded to a cap of three teams per institution.

2. Creating break rounds
You should create a round for every break round you intend to hold, including it in rounds.csv if using importtournament, or adding them under Tournaments > Rounds if using Edit Database. Be careful to set the following fields correctly:

- Break category must be set to the relevant break category.
- Stage and draw type must both be set to “Elimination”.

3. Setting break eligibility
Once a break category has been created it will not have any teams eligible for it, even if it was marked as “Is general”. To edit the eligibility of teams for any break round go to the Breaks item in the left-hand menu for a particular tournament and then click Team Eligiblity.

Here you can select “all” or “none” to toggle all team eligiblities or edit them using the tick boxes. Once you save it should return you to the main break page which will display the number of teams marked eligible.

Note
- Adjudicators can be marked as “breaking” on the Feedback page; clicking Adjudicators on the breaks page will take you straight there.

### Generating the break
Unlike team or speaker standings, each category’s break (and the break ranks of teams) are not determined automatically and updated continuously. Instead each can be generated (and regenerated) as desired.

To do so go to the Breaks item in the left-hand menu and then click the white button that corresponds to the break category you’d like to determine the rankings for. When prompted, select Generate the break for all categories to display the list of breaking teams.

From this page you can update the breaking teams list for this break category (or all categories) as well as view and edit ‘remarks’ that account for cases in which a team may not break (such as being capped or losing a coin toss).

Caution
- Please double-check the generated break before announcing or releasing it. Although the break generation code is designed to handle edge cases, we don’t test the code for such cases.

### Creating draws for break rounds
Creating a draw for a break round proceeds as normal, except that the team availability process is skipped. Instead, when you visit the availability page for that round it will have automatically determined which teams should be debating based upon the determined break for that category. Once a draw has been generated it will then use the relevant break ranks to create the matchups (ie 1st-breaking vs 16th-breaking, 2nd vs 15th, etc.). Subsequent break rounds will then also automatically determine matchups based on the previous round’s results and room ranks.

If the “break size” of a break category is not a power of 2, it will treat the first break round as a partial-elimination draw and only create a draw for the teams not skipping the partial-elimination round. Subsequent break rounds will then process as described above.

## Check-ins
A ‘Check-in’ is a record of a speaker, adjudicator, venue, or ballot’s status at a particular point in time. Typically these are used at large tournaments to reliably track who is or is not present for the first round of each day.

Check-ins serve a similar purpose to the availability system. However availabilities are tied to a particular round rather than to a particular time — they are generally used to record instances where you know ahead of time whether a person should or should not be included in a draw. In contrast, check-ins are useful for when you don’t know ahead of time whether a person will be able to be put into the draw and so want to be able to confirm their presence with a high degree of confidence. That said the two systems interact — the standard availability pages allow you to easily set all adjudicators or teams who have checked-in as available for a given round.

### Check-In Identifiers
Check-ins are associated with a ‘identifier’ — a number that is unique to each speaker and adjudicator. To generate these numbers go to the Identifiers section under the Check-Ins menu. From here you generate identifiers for Speakers, Adjudicators, and Venues as needed. Note also that Identifiers can be manually added or edited in the Edit Database area if necessary.

Once this number has been generated it can be transformed into a barcode so that it can be easily included on tournament badges or otherwise printed and disbursed. On the same Identifiers page you can use the View barcodes option to open up a page that lists all the barcodes for the speakers, adjudicators, or venues.

Note
- The identifiers for ballots are automatically generated when printing ballots.

### Recording Check-Ins
On the Scanning section of Check-ins you can record a particular check-in. This can be done in a few different ways:
1. You can type in the Identifier number into the box. Once five numbers have been identified it will automatically issue the check-in and clear the input field for the next number.
2. If you have purchased barcode scanners and configured them as USB keyboards they should then be compatible with this page: upon page load the cursor should be positioned in the input field, and any scanned barcodes should populate it with the specified number, issue the check-in, and then clear the box for the next scan.

Note
- Barcode scanners are probably cheaper than you think. A perfectly serviceable model should be around $20 USD or less although a cursory Google search might at first turn up models that are many times that amount. If you are a curious tab director, or are involved in a tournament with a little spare money, having just one or two around for critical tasks can be highly valuable.

3. If your device has a (web)cam you can use the Scan Using Camera button. Any barcodes put in front of the camera’s video stream will be scanned into the form. A sound will play when a barcode has been identified — so be aware that turning sound on or using headphones can help identify when a scan has been made.

Note
- Camera scanning works on most modern browsers although it will only work with Safari 11 or higher (iOS 11+ and macOS 10.13+). Camera scanning may also not work when using a local-installation of Tabbycat in all browsers, except Firefox where it seems to. Depending on the quality of your camera barcodes that are less than 4cm wide may not be recognised — ideally barcodes should be at least 5cm if using this method as your main way of checking-in things.

4. The Check-in status page (described below) allows assistants and administrators to manually check-in particular people or entire institutions without needing to know their identifiers.

### The Check-In ‘Window’
Because Check-In events are not explicitly linked to rounds there is essentially a ‘window’ or time period in which a check-in is still considered valid. The time of this ‘window’ in hours can be set in Setup > Configuration > Data Entry.

At tournaments the run check-ins during the start of each day the check-in ‘window’ (i.e. the time before check-ins expire) you can leave this window setting at the default time (12 hours) which should give enough time to distinguish between the first check-ins of that day as compared to the last check-ins of the previous day. At tournaments where you want to run a check-in process at the start of every round you may want to set the time to around 2 hours or something much shorter.

### Viewing Check-Ins
On the People Statuses section of Check-ins you can view who has or has not been checked-in. This page will live-update with the latest check-ins so you should be able to leave it open to monitor income attendances.

The blue “tick” boxes allow you to manually check-in people and/or entire institutions (for People) or venues and/or venue groups (for Venues) , without the need to scan their identifiers. This style of check-in is designed for use an auditorium roll-call type situation where you might be running through a list of people to the room or identifying absences on a per-institution basis.

Note
- A public version of this check-in status page can be enabled under Setup > Configuration > Public Features which can be useful for allowing people to self-police check-ins and/or validate their check-in worked.

### Check-Ins for Ballots
Ballots can be checked-in to quickly validate which ballots are physically present in the tab room. This can help more quickly identify ballots that are missing. Which ballots have or have not been checked-in will show up on the Results page. Ballots can be scanned using the standard ‘Scan Identifiers’ page.

Barcodes are automatically assigned and included to ballots when they are printed. Barcodes have no check-in window — any relevant check-in event counts regardless of how long ago it was.

### Check-Ins for Venues
Venues can be checked-in, but what a ‘venue check-in’ means is a bit more flexible. It might be used to validate which rooms are debate-ready at the start of a day (i.e. unlocked; has a desk) or it could be used during the rounds to record which rooms have returned their ballots.

Venues have a separate check-in window setting to that of people.

Venues have their own Status page (like people) and can be checked-in there manually. Like speakers and adjudicators their barcodes can also be printed off.

## Entering Ballots and Feedback
### Ballot check-in
For tournaments that require it, there is a “ballot check-in” page that can be used to record the arrival of ballots to the tab room. When there’s a missing ballot, it can help establish whether the ballot never made it to the tab room, or whether it’s probably floating around in the room forgotten. Also, it can help enforce early checks that panels return the correct number of ballots to the room.

To get to the ballot check-in, click the relevant round in the menu of the admin area, and then click “Results” and then “Ballot Check-In”. This requires superuser privileges.

There’s no adverse effect from not using the ballot check-in. Data enterers will still be able to enter and confirmed ballots, even if not checked in.

Tip
- Since the ballot check-in tends to require a dedicated computer or two, it can be worth creating a separate superuser account for ballot check-in, so that it doesn’t appear on the action logs as being by a particular person.
- Don’t forget to provision a computer or two for this if you’re planning to use it.
- Ballot check-ins can be a bottleneck, so you might decide they’re not worth using. Alternatively, you might have multiple computers for this purpose, or you might dedicate a tab room helper to driving the process (since this is probably faster than runners doing the typing in turn).

### Ballot entry
Most tab rooms run some sort of check system to ensure data is entered accurately. In Tabbycat, this is built into the system, which also helps speed it up.

As a general principle, Tabbycat requires all ballots to be looked at by two people. The first person enters the data from the ballot, and the second person checks it. The second person isn’t allowed to modify the data—they either confirm it or reject it, and if they reject it, then the whole process starts again. This is by design: to be confirmed, the same data must have been seen by at least two people.

Debates can be postponed either before or after a ballot is submitted. In this state, the ballot is ignored for the purposes of draw generation, so a draw can be created without having confirmed all ballots. This can also be useful to mark ballots for further inspection. This feature must be enabled in the Data Entry preferences.

Caution
- The administrator area does not work like this. It’s designed to be flexible, so allows you to edit, confirm or unconfirm any ballot at any time. For this reason, you should use the assistant area to enter ballots, even if you have a superuser account.

Tip
- Don’t forget to check the totals against the ballot—they’re a useful integrity check too.
- Don’t forget to check the winner against the ballot! If the adjudicator gets it wrong, it’s worth asking to clarify.
- It can be helpful to think about the room layout to maximize efficiency.
- Some tab rooms like to assign some to data entry and some to verification. This isn’t really necessary, since Tabbycat doesn’t let the same person enter and verify the same ballot. (This is one of many reasons why every person should have their own account.)
- Emails can be configured to be sent to adjudicators as a receipt of their ballot once confirmed.

### Duplicate/Swing Speeches
When entering the ballots there is a toggle label ‘Iron’ speeches. When set to “yes” this allows you to have the same speaker deliver multiple speeches provided their extra speeches are labelled on the form as ‘duplicates’. Typically, most tournaments require that the lesser ‘iron-person’ speech is discarded from the tab, which would mean that you would mark the lower speaker of the two scores as the duplicate (note that this may require you to check each score’s average across a panel).

Speeches marked as duplicates are not included in the speaker tab. This means that they can also be used to exclude swing speakers from the tab as needed; even if they do not actually speak twice. To do so, change the name of the swing speaker to be that of an existing team member and ensure that that speech is marked as a duplicate.

Tip
- There is also an option under Standings in the Configuration section that specifies the number of debates a speaker can miss before you will not show on the tab. By default there is no limit, but if need be this can be set to hide swing speakers from the final speaker tab.

### Feedback entry
Feedback doesn’t have the same verification process as ballots. Feedback that is entered by the tab room is assumed to be confirmed. If feedback is entered multiple times, all copies are retained but only the last one “counts” (is considered confirmed).

### Online entry
There are two methods of allowing ballots and feedback to be submitted online. Both are set in the Data Entry page of each tournament’s Configuration section and can be set independently; both in whether each can be submitted online at all and in which method of online submission are available.

### Private URLs
The first method of data entry is using ‘private URLs’. When this setting is enabled you can create a special URL that is unique to a participant. This link contains a number of random characters and is not displayed publicly; it is in effect a secret that only that a specific participant should know. Presuming people do not share these links to others, this provides a means to (relatively) securely identify who is submitting what information. Because Tabbycat knows which participant has which URL it will only allow them to submit feedback/ballots for debates that they were speakers/adjudicators in.

Warning
- Private URLs should provide more than adequate security for almost all tournaments’ purposes, but they aren’t foolproof. Anyone with access to the URL for a participant can submit feedback or ballots on their behalf, so it’s important that participants not share their URLs. This also means participants need to be careful when submitting from devices they do not own, because the URL will be logged in that device’s browser history.

These links must be generated within Tabbycat after the preference is enabled. To do so go to the Feedback section and then the Private URLs area. Once there you will be prompted to generate those URLs for all participants, which — once generated — will be presented in separate tables (one for teams; one for adjudicators).

These URLs can then be distributed to each person in a number of ways. There are pages within Tabbycat for printing them out (one URL per page labelled by recipient) or emailing them out (providing participants have been assigned email addresses). In the past tournaments have also used data from this table to send out SMSs by bulk, or distributed them to institutional representatives to disburse.

Tip
- You can assign email address to participants using the importtournament command when importing your registration data, or by going to the Edit Data area and looking up each Speaker/Adjudicator.
- If, after generating the private URLs, you add additional Teams or Adjudicators you can go to the Edit Database area , look up each Speaker/Adjudicator, and type in a bunch of random characters as their Url key to assign them a private URL.
- You can delete the current set of URLs by running this command in a shell on your server (replacing TOURNAMENT_SLUG with the appropriate value): python manage.py privateurls delete --tournament TOURNAMENT_SLUG

### Public URLs
The second method of data entry is using ‘normal URLs’. This essentially means that any users visiting the public version of the site is able to submit a ballot or feedback (as specified by their respective settings). They do so by self-selecting which Team or Adjudicator they are then entering in a form as normal.

This is, rather obviously, not a particularly secure method of data entry — nothing is stopping anyone on the site from entering data as someone else. The data can be checked, verified, and edited as normal by admins however. As such, this method is only recommended for small tournaments where you can trust those present to enter accurate information (or where accuracy is not crucial).

Tip
- There is an additional setting to set a ‘tournament password’ that needs to be submitted to enable the form. It is imagined, that if enabled, this password would only be distributed to tournament participants. However this only helps (at best) prevent non-participants from entering information; the fundamental problem of not verifying who is submitting what information is still present.

## Draw Generation
The draw generator is quite flexible. You can specify a number of settings to suit different tournaments’ rules.

### Summary of options
Options are set in the Configuration page as described in starting a tournament.
- Odd bracket resolution
  - How to resolve odd brackets
  - Allowable Values
    - Pull up from top
    - Pull up from bottom
    - Pull up from middle
    - Pull up at random

    - If sides are Random or Balance:
      - Intermediate
      - Intermediate with bubble-up-bubble-down

    - If sides are Pre-allocated:
      - Intermediate 1
      - Intermediate 2

- Side allocations method (how to allocate affirmative/negative)
  - Random
  - Balance
  - Pre-allocated
  - Manual ballot

- Pairing method (How to pair teams within brackers)
  - Slide
  - Fold
  - Adjacent
  - Random

- Conflict avoidance method
  - Off
  - One-up-down
  - Minimum cost matching

- Pullup restriction
  - No restriction
  - Choose from teams who have been pulled up the fewest times so far
  - Choose from teams with the lowest draw strength by speaks so far

Caution

The valid options for intermediate brackets change depending on whether sides are pre-allocated, but these are not checked for validity. If you choose an invalid combination, Tabbycat will just crash. This won’t corrupt the database, but it might be momentarily annoying.

The big picture
When generating a power-paired draw, Tabbycat goes through five steps:

First, it divides teams into “raw brackets”, grouping them by the number of wins.

Second, it resolves odd brackets, applying the odd brackets rule to make sure there is an even number of teams in each bracket. This is often called “pulling up” teams.

Third, within each bracket, it pairs teams into debates using the pairing method.

Fourth, if enabled, it adjusts pairings to avoid conflicts.

Finally, it assigns sides to teams in each debate.

For each of these steps except the first, Tabbycat allows you to choose between a number of different methods.

### Explanations of options
#### Odd bracket resolution
The draw odd brackets option specifies what you do when a bracket has an odd number of teams. (Obviously you have to do something, otherwise you can’t pair off teams within the bracket.) There are two groups of methods: pull-up and intermediate brackets.

- Pull-up methods take one or more teams from the next bracket down, and move them into the odd bracket to fill the bracket.

- Intermediate brackets take the excess teams from the odd bracket and move them down into a new bracket, which sits between the odd bracket and the next one down (the “intermediate bracket”). It then takes teams from the next bracket down and moves them up to fill the new intermediate bracket.

The exact mechanics depend on whether or not sides are pre-allocated.

#### When sides are not pre-allocated
- Pull-up methods: Take a team from the next bracket down, and add them to the odd bracket to form an even bracket. You can choose to pull up the top team from the next bracket, or the bottom team, or the middle team, or a randomly chosen team. (If you pull up the middle team, and the bracket has an even number of teams, then it will choose randomly from the two middle teams.)
- Intermediate brackets: Take the bottom team from the odd bracket and match them against the top team from the next bracket. An intermediate bracket always has two teams.
 If you’re using conflict avoidance and intermediate brackets, you will probably want to use Intermediate with bubble-up-bubble-down instead. This uses the “bubble-up-bubble-down” rule to swap teams out of an intermediate bracket if there is a history or institution conflict. This is defined in the Australs constitution and is analogous to the “one-up-one-down” rule.

Caution
- Using Intermediate with One-up-one-down does not imply Intermediate with bubble-up-bubble-down. You must enable Intermediate with bubble-up-bubble-down specifically.

#### When sides are pre-allocated
When sides are pre-allocated, an “odd bracket” is one that has an uneven number of affirmative and negative teams. (So odd brackets can have an even number of teams, e.g. 4 affs and 2 negs.)

- Pull-up methods: Take as many teams from the next bracket down as necessary to fill the bracket. If there aren’t enough teams in the next bracket down, take teams from the bracket after that, and so on, until the (original) odd bracket is filled. Higher brackets are always filled first. You can choose to pull up the top teams from the next bracket, the bottom teams, or a random selection of teams.

- Intermediate brackets: Take the unpaired teams in a bracket, and move them down to a new intermediate bracket. Then, take the number of teams necessary from the opposite side, from the next bracket down, to fill the next bracket.
Intermediate 1 and Intermediate 2 differ only in what happens if there aren’t enough teams in the next bracket to fill the intermediate bracket. In Intermediate 1, it will just take teams from the bracket after that, and so on, until the intermediate bracket is filled. In Intermediate 2, it will split the intermediate bracket: the teams that can be paired with the next bracket form the first intermediate bracket, and then the teams that aren’t form a new (unfilled) intermediate bracket, to be filled from teams from the bracket after that. This keeps going, splitting into as many intermediate brackets as necessary, until all excess teams from the original odd bracket are paired.

### Side allocations
There are four methods:
- Random allocates randomly. Some tournaments might like this, but most will probably want to use Balance, because Random doesn’t guarantee that a team won’t be (say) affirming the entire tournament.
- Balance assigns the team that has affirmed less so far the affirmative side (and, therefore, the team that has negated less the negative side). If both teams have affirmed the same number of times, it assigns sides randomly.
- Preallocated is used for pre-allocated sides. If used, you must enter data for pre-allocated sides into the database, as specified below.
- Manually enter from ballot is used for tournaments where the sides of the teams involved are not assigned in advance, but are instead determined by the teams themselves

### Pre-allocated sides
There isn’t currently any way to edit side allocations from the front end. To do so from the back end, you need to create one TeamPositionAllocation entry for each team in each round. All teams must have an allocation for every round. There are a few ways to do this, take your pick:
- If you’re using the importtournament command, it reads sides from the file sides.csv.
- You can do this from the Django admin interface (under Setup > Edit Database) by going to the relevant team and adding a team position allocation entry. That is:
    1. Click Admin on the bottom right of any page after logging into an account with superuser access.
    2. Next to Teams, click Change.
    3. Click on the name of the team you want to edit side allocations for.
    4. Add or edit the entry or entries in the Team position allocations table at the bottom.
- You can also do this by writing a script that creates TeamPositionAllocation objects and saves them. Have a look at draw/management/commands/generatesideallocations.py for an example.

### Pairing method
It’s easiest to describe these by example, using a ten-team bracket:
- Fold: 1 vs 10, 2 vs 9, 3 vs 8, 4 vs 7, 5 vs 6. (Also known as high-low pairing.)
- Slide: 1 vs 6, 2 vs 7, 3 vs 8, 4 vs 9, 5 vs 10.
- Adjacent: 1 vs 2, 3 vs 4, 5 vs 6, 7 vs 8, 9 vs 10. (Also known as high-high pairing.)
- Random: paired at random within bracket.

Teams are always paired within their brackets, after resolving odd brackets.

### Conflict avoidance method
A conflict is when two teams could face each other but should not, possibly for a variety of reasons. Some tournaments have a preference against allowing this if it’s avoidable within certain limits. The draw avoid conflicts option allows you to specify how.

You can turn this off by using Off. Other than this, there are currently two conflict avoidance methods implemented.

One-up-one-down is the method specified in the Australs constitution. This method only considers conflicts for teams that have seen each other before, or are from the same institution. Broadly speaking, if there is a debate with a conflict:
- It tries to swap teams with the debate “one up” from it in the draw.
- If that doesn’t work, it tries to swap teams with the debate “one down” from it in the draw.
- If neither of those works, it accepts the original conflicted debate.

It’s a bit more complicated than that, for two reasons:
- History conflicts are prioritised over (i.e., “worse than”) institution conflicts. So it’s fine to resolve a history conflict by creating an institution conflict, but not the vice versa.
- Each swap obviously affects the debates around it, so it’s not legal to have two adjacent swaps. (Otherwise, in theory, a team could “one down” all the way to the bottom of the draw!) So there is an optimization algorithm that finds the best combination of swaps, i.e. the one that minimises conflict, and if there are two profiles that have the same least conflict, then it chooses the one with fewer swaps.

Minimum cost matching is a more flexible method designed for APDA and other formats. This method creates a graph between teams in a bracket, weighing all possible pairings for conflicts, and finding the minimum weight matching with the Blossom algorithm. In addition to history and institution conflicts, it can try to minimize the number of times teams have seen a pulled-up team, and stabilize side balance.

### Pullup restriction
You can restrict which teams can be pulled up by configuring the draw generator to choose a pullup team from among only those teams who are the “best off” according to a given metric. If several teams are equally “best off” within the lower bracket, the draw generator chooses among them using the same pull-up method already specified (e.g., “pull up from top”)

- You can choose from teams who have been pulled up the fewest times so far, that is, in rounds before the current round. Most of the time, this is equivalent to saying that a team cannot be pulled up more than once. But if all teams in a bracket have been pulled up at least once, it then chooses from among teams who have been pulled up only once (if any), and so on.

- You can choose from teams with the lowest draw strength so far, by wins or speaks.
If you choose speaks, it’s unlikely that two teams will have the same draw strength by speaks, so most of the time this will just choose the team in the lower bracket that’s had the easiest draw so far (as measured by their opponents’ speaker scores).

Pullup restrictions only apply when the odd bracket resolution method is a pullup method. They have no effect on intermediate brackets.

## Draw Generation (British Parlamentary)
The draw generator for British Parliamentary tournaments tries to rotate teams through positions by assigning them positions they’ve been in less often before the current round.

### Summary of options
Options are set in the Configuration page as described in starting a tournament. Options in italics with an asterisk are not WUDC-compliant. The recommended options are shown in bold.
- Pullup distribution (Where pullup teams get placed)
  - Anywhere in bracket
  - All in the same room*
- Position cost (Which cost function to use to indicate which position profiles are preferred)
  - Simple
  - Rényi entropy
  - Population variance 
- Rényi order (Order of Rényi entropy)
  - Any non-negative number (default: 1, i.e. Shannon entropy)
- Position cost exponent (Degree to which large position imbalances should be prioritised)
  - Any non-negative number (default: 4)
- Assignment method (Algorithm used to assign positions)
  - Hungarian*
  - Hungarian with preshuffling

### The big picture
To try to achieve position balance, Tabbycat treats the allocation of teams to debates as an assignment problem. That is, it computes the “cost” of assigning each team to each position in each debate, and finds an assignment of all teams to a position in a debate that minimises the total cost (the sum over all teams).

#### A simple example
Here’s a small example, to illustrate the idea. Say you have a tournament with 16 teams, and you’re about to draw round 4. There are sixteen “places” in the draw: four positions in each of four rooms. Tabbycat calculates the “cost” of putting each team in each place, and puts them in a matrix. 

Each “16” is the cost of putting a team in a position it’s seen once; each “0” is the cost of putting a team in the position it hasn’t. (Details of how this is calculated are below.) For example, team A (on 8 points) has been in every position except CO. The ∞’s indicate places where the team isn’t allowed to go, because the room isn’t in their bracket. For example, the three teams on 6 points (D, E, F) can go in either the top or second room, because any of them can be the pullup team.

The algorithm then chooses entries so that one is selected from each row and one is selected from each column, in a way that minimises the sum of the selected entries. In this case, the selected entries are highlighted in blue. For example, the top room comprises teams E (OG), B (OO), C (CG) and A (CO).

Sometimes, particularly in round 4, it simply isn’t possible to “satisfy” everyone. For example, among the top eight teams, five haven’t been in OO, but only two can be accommodated within those brackets. In this case, teams B and G got lucky; there are also many other draws that would have incurred the same total cost.

More generally, in most cases, there will be many optimal solutions. To randomise the selection among them, Tabbycat (under default settings) randomly permutes the rows and columns of the matrix before starting the assignment algorithm.

### Explanations of options
#### Pullup distribution
If the number of teams in a bracket is not a multiple of four, it pulls up teams from the next bracket down. The pullup distribution then governs how those teams are paired into the upper bracket.

The available options are as follows:
- Anywhere in bracket: The pullup teams are treated as if they were any other team in their new bracket. For example, if there are 17 teams in a 10-point bracket, then the three 9-point teams that get pulled up may be paired anywhere in the 10-point bracket, independently of each other. Chance might put them in the same room, but more likely, they will not all be in the same room, so there will be multiple pullup rooms in the 10-point bracket.
- All in the same room: All of the pullup teams will be paired into the same room. This means that there will be at most one pullup room per bracket, effectively creating an “intermediate bracket”.

Note
- While it can be argued that the All in the same room setting is fairer, it is prohibited by the WUDC constitution. If your tournament follows WUDC rules, you cannot use this setting. The teams that get pulled up aren’t specifically chosen—they’re just assigned as part of the algorithm described above, which optimises for position balance. Tabbycat doesn’t support taking anything else into account when choosing pullup teams. (WUDC rules wouldn’t allow it, either.)

#### Position cost options
The position cost function is a function that indicates how “bad” it would be if a team were to be allocated a certain position (OG, OO, CG, CO) in a debate. When generating a draw, Tabbycat chooses from among the draws that minimise the sum of the position costs for each team.

More formally:
A position history or just history \mathbf{h} is a 4-tuple where each element is the number of times a team has already been in the corresponding position. For example, \mathbf{h} = (0, 2, 1, 1) means that a team has been in OO twice, CG and CO once each, and hasn’t been in OG.

A cost function C(\mathbf{h},s) is a function specifying how “bad” it would be if a team with position history \mathbf{h} were assigned the position s in the next round.

Tabbycat allows you to choose from a number of different position cost functions, as well as a position cost exponent \beta. Then, when allocating teams to debates, Tabbycat allocates teams to positions (s_t, t \in\mathcal{T}) to minimise

\sum_{t \in \mathcal{T}} [C(\mathbf{h}_t,s_t)]^\beta

where \mathcal{T} is the set of all teams, \mathbf{h}_t is the position history of team t and s_t is the position to which team t would be allocated.

#### Position cost exponent
The position cost exponent \beta controls how different teams trade off with each other.
- The larger \beta is, the more concerned it is with preventing very bad situations. That is, it will give more teams some slight unevenness in order to prevent one team from getting a very uneven history.
- The smaller \beta is, the more concerned it is with preventing any unevenness. That is, it will try to keep more teams from being uneven at all, at the cost of possibly letting just one team get a very uneven history.
- At the large extreme, as \beta\rightarrow\infty, it will do everything it can to minimise the plight of the worst-off team, and it won’t care for any team other than the worst-off.
- At the small extreme, as \beta\rightarrow 0, it will do everything it can to minimise the number of teams with a non-optimal profile—but if it’s impossible to protect a team from sub-optimality, it won’t care how uneven the unlucky team gets.

The “balanced” approach would be \beta = 1, which just takes the cost function as-is. This doesn’t mean that this is the best idea, however—you’d typically want to bias towards preventing very uneven histories a bit more. Most tournaments will probably want \beta to be somewhere between 2 and 5. (Note that \beta need not be an integer.)

#### Position cost functions
Tabbycat allows you to choose between three position cost functions C(\mathbf{h},s): Simple, Rényi entropy and Population variance.

In the descriptions that follow, \mathcal{S} = \{\texttt{OG}, \texttt{OO}, \texttt{CG}, \texttt{CO}\}, the set of all BP positions.

##### Simple
The simple cost function C_\textrm{simple}(\mathbf{h},s) returns the number of times the team has already been in position s, less the number of times the team has been in its least frequent position. That is,

C_\mathrm{simple}(\mathbf{h},s) = \mathbf{h}[s] - \min_{s' \in\mathcal{S}} \mathbf{h}[s']

where \mathbf{h}[s] is the element of \mathbf{h} corresponding to position s.

##### Rényi entropy
Informally speaking, the Rényi entropy is a measure of the diversity of the positions in a team’s history. A history consisting only of one position has low entropy, while a history that is perfectly evenly distributed has high entropy. The Rényi entropy cost function reverses this intuition, so that an even hypothetical history has low cost, while an uneven hypothetical history has high cost.

The Rényi entropy takes one parameter, known as its order, \alpha, which will be further discussed below.

More formally, the Rényi entropy cost function C_\textrm{R\'enyi}(\mathbf{h},s) is defined as

C_\textrm{R\'enyi}(\mathbf{h},s) = n_\mathbf{h} [2 - H_\alpha(\hat{p}_{\mathbf{h},s})]

where

- n_\mathbf{h} = \sum_{s'} \mathbf{h}[s'] is the number of rounds the team has competed in so far.

- \hat{p}_{\mathbf{h},s} is the normalised hypothetical position history that would arise if a team with history \mathbf{h} were to be allocated position s in the next round; that is,

  \hat{p}_{\mathbf{h},s}[s'] = \begin{cases}
    \frac{1}{n_\mathbf{h} + 1} (\mathbf{h}[s'] + 1), &\text{ if } s = s', \\
    \frac{1}{n_\mathbf{h} + 1} \mathbf{h}[s'], &\text{ if } s \ne s'.
  \end{cases}

  Note that \hat{p}_{\mathbf{h},s} is a probability distribution (that is, its elements sum to 1).

- H_\alpha(\cdot) is the Rényi entropy of order \alpha of a probability distribution, defined as

  H_\alpha(p) = \frac{1}{1-\alpha} \log_2 \left( \sum_{s\in\mathcal{S}} (p[s])^\alpha \right), \qquad \alpha \ne 1.

  In the special (limiting) case where \alpha=1, it reduces to the Shannon entropy,

  H_1(p) =-\sum_{s\in\mathcal{S}} p[s] \log_2 p[s].

  Note that for all \alpha, 0 \le H_\alpha(p) \le \log_2(4) = 2 (since there are four positions in BP).

The Rényi order is the parameter \alpha above, and it controls what it means to be “even among positions” for a team. Note that “evenness” is not easily defined. After round 8, which position history is more even: (0, 2, 3, 3) or (1, 1, 1, 5)? The Rényi order allows us to tune this definition.

- The smaller \alpha is, the more it cares that teams compete in every position at least once, favouring (1, 1, 1, 5) over (0, 2, 3, 3): it’s worse to have never OGed, than it is to have COed five times.
- The larger \alpha is, the more it cares that teams do not compete in any (one) position too many times, favouring (0, 2, 3, 3) over (1, 1, 1, 5): it’s worse to have COed five times, than it is to have never OGed.
- At the small extreme, as \alpha\rightarrow0, it only counts how many positions a team has seen at least once, and doesn’t care about the distribution among them so long as a team has been in each position once.
- At the large extreme, as \alpha\rightarrow\infty, it only looks at how many times each team has seen its most frequent position, and tries to keep this number even among all teams.

The “balanced” approach would be \alpha=1 (the Shannon entropy), though of course it’s arguable what “balanced” means. Tabbycat defaults to this value.

To give some intuition for the useful range: In round 9, a strict ordering by number of positions seen at least once occurs for approximately \alpha < 0.742. A strict ordering by number of times in the most frequent position occurs for \alpha>3. Changing \alpha outside the range [0.742, 3] will still affect the relative (cardinal) weighting between teams, but will not affect the ordinal ranking of possible histories.

The purpose of weighting costs by n_\mathbf{h} is to prioritise those teams who have competed in every round over those who have competed in fewer rounds.

##### Population variance
The population variance cost function is just the population variance of the history 4-tuple,

C_\textrm{popvar}(\mathbf{h},s) = \frac14 \sum_{s'\in\mathcal{S}} \left(\mathbf{\hat{h}}_s[s'] - \mu_{\mathbf{\hat{h}}_s} \right)^2,

where \mathbf{\hat{h}}_s is the hypothetical position history that would arise if a team with history \mathbf{h} were to be allocated position s in the next round; that is,

\mathbf{\hat{h}}_s[s'] = \begin{cases}
  \mathbf{h}[s'] + 1, &\text{ if } s = s', \\
  \mathbf{h}[s'], &\text{ if } s \ne s'.
\end{cases}

and where \mu_{\mathbf{\hat{h}}_s} is the mean of \mathbf{\hat{h}}_s,

\mu_{\mathbf{\hat{h}}_s} = \frac14 \sum_{s'\in\mathcal{S}} \mathbf{\hat{h}}_s[s'].

At the extremes, a team that has seen all positions evenly will have a population variance of zero, while a team that has seen just one position n times will have a population variance of \frac{3n^2}{16}.

#### Assignment method
Tabbycat uses the Hungarian algorithm to solve the assignment problem of assigning teams to positions in debates. This can be run with or without preshuffling:
- Hungarian algorithm just runs the Hungarian algorithm as-is, with no randomness. This probably isn’t what you want.
- Hungarian algorithm with preshuffling also runs the Hungarian algorithm on the position cost matrix, but shuffles the input so that the draw is randomised, subject to having optimal position allocations.
  Preshuffling doesn’t compromise the optimality of position allocations: It simply shuffles the order in which teams and debates appear in the input to the algorithm, by randomly permuting the rows and columns of the position cost matrix. The Hungarian algorithm still guarantees an optimal position assignment, according to the chosen position cost function.

Note
- Running the Hungarian algorithm without preshuffling has the side effect of grouping teams with similar speaker scores in to the same room, and is therefore prohibited by WUDC rules. Its inclusion as an option is mainly academic; most tournaments will not want to use it in practice.

No other assignment methods are currently supported. For example, Tabbycat can’t run fold (high-low) or adjacent (high-high) pairing within brackets.

## Preformed Panels
Preformed panels, also known as a ‘shadow draw’, allow adjudicator panels to be created before a round has been drawn and then applied once its draw is ready. This means that panel formation can be done during periods outside the normal time pressure of finalising a draw for release. This can save a lot of time at large tournaments, or at tournaments where the adjudication core wants to carefully control the specific combination of adjudicators within panels.

Tabbycat’s provides two distinct workflows for employing preformed panels.

The first method, Direct Allocation is simple. A set of preformed panels as made ahead of time, and that collection of panels is transposed atop the draw. This allocation always applied panels linearly from top to bottom — it does not account for any information about each debate (e.g. conflicts) other than their position.

The second method, Smart Allocate is more powerful, but less simple. It employs Tabbycat’s existing allocation tools, primarily the notion of a debate’s priority, to allow for a non-linear matching of preformed panels that avoids adjudicator conflicts and better adapts to a given draw — particularly when the most important debates do not strictly follow the highest debate brackets.

This method relies on each preformed panel being assigned a priority value. When applying preformed panels to a draw, the allocator then ties to best match the priority value of each preformed panel to the priority of each actual debate. This is similar to how Tabbycat’s normal auto-allocator matches the strength of each panel (as measured by adjudicators’ ratings) to the priority of each debate.

### Step 1: Create preformed panels
You can find the preformed panels section either
- under the Setup menu (for all rounds), or
- on the Draw page (for the current and next round).

Initially, the preformed panels page will have no panels. Click the Create Panels button in the top left to make some. The panels it creates are based upon a projection of that round’s general results using the results of the previous round. As a result, each preformed panel will have a bracket range, the lowest and highest brackets that debate might be in, and a liveness range, the maximum number of teams that could be live in that room.

Note
- Like the normal adjudicator allocation interface, the preformed panel interfaces will indicate when an adjudicator has not been marked as available. If using preformed panels, you may want to set adjudicator availability earlier than you would otherwise.

Note
- Liveness in the anticipated draw only pertains to the open category (the first break category that is marked as a “general” category). It’s not possible to meaningfully predict where teams open-dead but live in other categories will end up.

### Step 2: Assign priorities to preformed panels
By default the priority slider for all preformed panels is in the neutral position. You can use the “Prioritise” button in the top left to assign priority values automatically, based upon their brackets or liveness. Before or after this step you can alter the priorities as usual — even after you have allocated adjudicators.

It’s important to remember to assign a range of priorities to the panels. Without distinct priority values, the application of your preformed panels to the actual draw will be essentially random. If allocating priorities manually, it is a good idea to keep a relatively even distribution of priorities — use the range!

Note
- In Round 1, each debate has a liveness and bracket of 0. If you are using preformed panels in this instance you may need to manually-differentiate their priorities.

Note
- This step is optional if you plan to use a Direct Allocation.

### Step 3: Allocate adjudicators to preformed panels
Now that your panels have a priority, you can begin allocating adjudicators. You can do this manually, but do note that the normal auto-allocator for adjudicators also works in this context (the “Allocate” button). Even if you want to tweak your panels extensively, the auto-allocator can provide a good first-pass collection of panels, because it will give stronger adjudicators to the panels that you have marked as important.

The created panels all auto-save, so you can leave the page and return to pick up where you left. Like the main allocation interface, changes should appear ‘live’ across different computers and the sharding system is available to divide up each person’s view of the draw.

### Step 4: Generate the draw
Proceed with the creation of the draw as usual. Open up the normal adjudicator allocation page for that round.

### Step 5: Assign priorities to debates
When allocating preformed panels, the priority levels are what connects the preformed panels to the actual debates. It is thus crucial that you assign priorities to the debates in the actual draw using automatic prioritisation or the manual sliders. Because the automatic prioritiser does not employ the highest priority value, it is worth having a look at the draw and seeing if any debates justify this before proceeding.

Note
- This step is optional if you plan to use a Direct Allocation, but can be useful as a way to tweak the order of debates before transposing the panels.

### Step 6: Allocate preformed panels to debates
To  allocate preformed panels to your debates, click the normal “Allocate” button and then select the Smart Allocate or Direct Allocate option.

This will then allocate the preformed panels to debates.

You can the edit the allocation as normal. If needed, you can redo the allocation of the preformed panels at any point.

### How does the ‘Smart Allocator’ work?
Roughly speaking, the allocator tries to match panel priorities to debate priorities, while avoiding conflicts. It’ll mostly try to swap panels within priority levels in order to avoid conflicts. If there aren’t exactly as many panels at each priority level as there are debates, it’ll do its best to match what it can.

More formally, it treats the allocation of preformed panels to debates as an assignment problem, with a cost of assigning each panel p to each debate d given by

C(p,d) = w_\mathrm{mism} [\mathrm{importance}(p) - \mathrm{importance(d)}]^2 + w_\mathrm{conf} \, \mathrm{conflicts}(p,d) + w_\mathrm{hist} \, \mathrm{history}(p,d)

where

w_\mathrm{mism} is the “Importance mismatch penalty” in the “Draw rules” settings,

w_\mathrm{hist} is the “Adjudicator conflict penalty” in the “Draw rules” settings,

w_\mathrm{conf} is the “Adjudicator history penalty” in the “Draw rules” settings,

\mathrm{importance}(p) is the importance of panel p,

\mathrm{importance}(d) is the importance of debate d,

\mathrm{conflicts}(p,d) is the number of adjudicator-team conflicts between panel p and debate d, and

\mathrm{history}(p,d) is the number of adjudicators and teams who have seen each other between panel p and debate d.

It then uses the Hungarian algorithm to find the assignment of panels to debates that minimizes the total cost of the pairings.

## Standing Rules
### Team standings rules
In Tabbycat, you can choose how teams are ranked in the team standings. For example, at Australs, teams are ranked first on the number of wins, and second on their total speaker score. The setting that specifies how teams are ranked is called the team standings precedence. The team standings precedence is used:
- When displaying the team tab,
- Whenever a power-paired draw is generated, and
- When computing which teams are in the break.

When you choose the team standings precedence, you choose from a list of metrics. Then, in the standings, teams will be sorted first by the first metric, then by the second metric, and so on. You must choose at least one metric, and you can choose up to eight. Teams tied on all metrics will have the same rank.

If you like, you can also choose team standings extra metrics, which are metrics that will be shown in the team standings, but not used to rank teams.

- Wins: How many debates the team has won.
- Points: How many points the team has. For two-team formats, this is just a synonym for wins, and differs only in column labelling. For BP, this is 3 points for a first, 2 for a second, 1 for a third and 0 for a fourth. Round weightings are taken into account.
- Total speaker score: The sum of all speaker scores attained in all debates.
- Average total speaker score: The average total speaker score over all debates the team has had, not counting debates where they or their opponents forfeited.
- Average individual speaker score: The total substantive speaker score, over all debates the team has had and the number of speakers. Provides an equivalent metric to average total speaker score in no-reply formats, but within the substantive speech scoring range.
- Speaker score standar deviation: The standard deviation of total speaker scores over all debates the team has had, not counting debates where they or their opponents forfeited. This metric is ranked in ascending order (smaller standard deviations ranked higher).
- Sum of margins: The sum of all margins. Wins are positive, losses are negative.
- Average margin: The average margin over all debates the team has had, not counting debates where they or their opponents forfeited.
- Draw strength by wins: The sum of the number of wins of every team this team has faced so far. This is also known in some circuits as win points, opponent wins or opponent strength.
- Draw strength by speaker score: The sum of speaker scores of every team this team has faced so far.
- Votes/ballots carried: The number of adjudicators that gave this team a win across all of their debates. Also known as the number of ballots or judges a team has. In cases where the panel is smaller or larger than 3, this number is normalised to be out of 3. For example, if a panel of five splits 3–2, then the winning team is recorded as gaining 1.8 votes, and the losing team is recorded as gaining 1.2. This also means that solo adjudicators are always worth three votes.
- Number of firsts: The number of debates in which the team came first. Only makes sense for British Parliamentary.
- Number of seconds: The number of debates in which the team came second. Only makes sense for British Parliamentary.
- Number of thirds: The number of debates in which the team came third. Only makes sense for British Parliamentary with variable round weights.
- Number of pullups before this round: The number of times the team has been pulled up as part of draw generation. You probably wouldn’t use this as a metric to rank teams, but you may wish to display it as an “extra metric” in the team standings for transparency.
- Who-beat-whom: If there are exactly two teams tied on all metrics earlier in the precedence than this one, then check if the teams have faced each other. If they have, the team that won their encounter is ranked higher. If they have seen each other more than once, the team that has won more of their encounters is ranked higher. If there are more than two teams tied, this metric is not applied. This metric can be specified multiple times. Each time who-beat-whom occurs, it applies to all the metrics earlier in the precedence than the occurrence in question.

### Speaker standings rules
The speaker standings precedence is only used in speaker standings (i.e., it doesn’t affect the operation of the tournament). As for team standings, the speaker standings precedence specifies which metrics are used to rank speakers, with the second metric tie-breaking the first, the third tie-breaking the second, and so on. The speaker standings extra metrics are metrics that will be shown in the speaker standings, but won’t be used to rank speakers.

- Total: The sum of all speaker scores attained by the speaker. Note that if a speaker misses a round, they’ll typically be relegated to the bottom of the speaker standings by this metric.
- Average: The average of all speaker scores attained by the speaker.
- Trimmed mean: The average speaker score after excluding their highest and lowest speaker scores. Also known as the high-low drop, truncated mean or Olympic average. If the speaker has only one or two scores, this metric just returns the average of those scores, without excluding any.
- Standard deviation: The standard deviation of all speaker scores attained by the speaker. This metric is ranked in ascending order (smaller standard deviations ranked higher).
- Average speaker score: The average total speaker score over all debates the team has had, not counting debates where they or their opponents forfeited.
- Number of speeches given: The number of speaker scores associated with the speaker. (In tournaments where teams can rotate speakers, this may not be all rounds.) This metric is normally used as an “extra” (unranked) metric, because it’d be weird to rank by number of speeches given, but you can if you want to.

### The motion balance page applies a statistical test to estimate the degree to which a motion is imbalanced. This is calculated by first making an underlying assumption that a motion is generally fair. This will be our null hypothesis: that, for a given motion, affirmative teams won the same number of times as negative teams.

Our chi-squared test will then be centred around disproving this hypothesis. If we disprove the hypothesis, we say that, in the context of this tournament and this draw, the motion ended up being unbalanced. However (technically speaking) if we fail to reject the null hypothesis, we would conclude that there is insufficient evidence to suggest that the motion was unbalanced in the context of this tournament.

The test proceeds by calculating the chi-squared stat, then running a series of tests. The tests are where we go a little off-book with respect to statistical methodology. Normally we would test at a single “level of significance” (ie. with a certain degree of certainty), but that’s insufficient in telling us how bad a motion ended up being. So, instead, we conduct a range of tests with a range of levels of significance, and calculate the minimum level of significance that causes our null hypothesis to be rejected. Using the minimum level of significance that rejects our null hypothesis, we can then grade the fairness of the motion on a scale. Motions whose tests fall below a certain threshold will be considered fair, while others will be graded based on the minimum.

For formats with topic selection, the same test is applied using the number of affirmative and negative vetoes in place of wins. The assumption here is that, during the time allotted for motion selection, teams estimate how appealing a motion is from their position, and then veto the topic that they feel is least favourable. Thus, the null hypothesis is that a motion that is perceived of as fair would be vetoed by affirmative and negative teams to an equal degree.

## User accounts
For obvious reasons, user logins are required to data entry and administrative functions. Conceptually, there are four levels of access:
- Public (Publicly available information):  Viewing things, and submitting new ballots/feedback if electronic submission is permitted by the tournament.
- Assitant (assistant area): Entering, confirming and printing ballots and feedback, checking in ballots and people, and displaying the draw.
- Superuser (The administrator and assistant areas): Generating draws, allocating adjudicators and venues, and editing ballots, feedback and adjudicator scores.
- Staff and superuser (The administrator, assistant and Edit Database areas): Editing the database directly.

If a user account on the tab system belongs to someone who is also a participant in the tournament (e.g., a chief adjudicator), these two capacities are completely separate. User accounts are only used to regulate access to administrative functions. Tabbycat doesn’t know about any relationship between user accounts, and who is participating in the tournament.

### Account roles
You should create an account for each person who needs to access the tab system. When you create an account in the Edit Database area, there are checkboxes for Superuser status and Staff access. Superusers have access to the administrator area, and staff have access to the Edit Database area. You should grant permissions as follows:

- Tab directors should get both superuser and staff status.
- Chief adjudicators and their deputies should get superuser status, but not staff status.
- Tab assistants (helping only with data entry) should get neither superuser nor staff status.

Tournament participants (other than tab staff) do not need an account. Everything they need to know can be accessed without an account. If you’re using electronic ballots or electronic feedback, they access these using a URL that only they know (see Private URLs).

When doing data entry, users with superuser status should use the assistant area. The administrator area is intended for managing the tournament, and should not in general be used for data entry. Specifically, the administrator area lacks checks that are important for data integrity assurance. It should be used only to override the normal data entry procedure, for example, to unconfirm or modify a ballot.

The Edit Database interface should not be used except where it is actually necessary. There are a few functions which require this, but as a principle, it shouldn’t be used as a matter of course.

Note
- In theory, you could grant an account staff status but not superuser status. But then they’d be allowed to edit the database, but not run the tournament, which would be weird.

### Allow users to create accounts.
If you wish to allow select staff to create their own accounts, you can do so:
1. Go to the Configuration area of any tournament.
2. Select the Global Settings section.
3. Specify a secret password for the types of account creation you wish to enable. This should be hard to guess (don’t just use “Admin” or your tournament name).
4. Provide the password of the desired account type to people needing an account. This password is part of a link to the signup form. This form is available with the URL path /accounts/signup/KEY/, replacing KEY with the password.

Note
- It is not possible to create a link that automatically gives super-user access. You should either manually create other superusers, or use the admin interface to promote them once they have created an account this way.

### Adding accounts manually.
To add an account:
1. Go to the Edit Database area of the site.
2. Under Authentication and Authorization, click the Add link next to Users.
3. Ask the user to enter a username, password and possibly email address.
  - Only they should know what the password is.
  - If you’re hosting on the internet, all passwords should be at least moderately strong!
  - Passwords are not stored as raw passwords, so you can’t figure out what their password is.
  - The email address is optional.
  - This email address is only used to reset their password if they forget it, and has nothing to do with the email address that Tabbycat uses to send emails to tournament participants (e.g. private URL links).
4. If they are being assigned superuser and/or staff status, check the relevant boxes.
5. Click “Save” or “Save and add another”.


## Venue Constraints
Tabbycat supports a basic form of venue constraints. A venue constraint is a requirement that a particular team, adjudicator, institution or division be assigned to a venue in a particular venue category. Typical uses would include:

- Meeting venue accessibility requirements of particular teams (e.g. step-free access)
- Placing adjudication core and tab team members close to the tab room
- Keeping all debates in a division in one location

Constraints apply to venue categories, not individual venues. That is, you specify that (say) a team should be given a venue from a particular list of venues. Of course, it’s permissible for a venue category to have only one venue in it.

The algorithm used to satisfy venue constraints is not guaranteed to be optimal. In some rare cases, it may propose an allocation that fails some constraints, even though some other allocation would have satisfied all (or more) constraints. In almost all practical circumstances, however, it should work, and save human effort (and time) in specially allocating rooms.

### Adding venue categories
Before you add venue constraints, you first need to add venue categories. Each venue category is a list of venues, typically satisfying a particular need. For example, you might have a category for each of the following:

- Venues with step-free access
- Venues that are close to general assembly (the briefing room)
- Venues that are close to the tab room
- Venues that are, or venues that are not, being live-streamed

Each venue can be in as many categories as you like (or none at all).

To add or edit venue categories, go to the Import Data area (under Setup) then select Add/Edit Venue Categories. Note that this page will show all existing Venue Categories first before showing the blank forms that allow you to create new categories. Give your category a name (like “Step-free access”), assign it some venues, then click the “Save Venue Categories” button at the bottom of the page.

Alternately you can add or edit a venue category by going to the Edit Database area (under Setup), scroll down to “Venues” and click “Venue categories”. Then click the + Add venue category button in the top-right of the page or click an existing item.

### Adding venue constraints
To add or edit venue constraints, go to the Import Data area (under Setup) then select Add/Edit Venue Constraints. Note that this page will show all existing Venue Constraints first before showing the blank forms that allow you to create new categories. Note that the “Constrainee ID” field should let you select from a dropdown or type in the name of an adjudicator, institution, or team (rather than having to lookup the exact ID).

Alternately you can add or edit a venue category by going to the Edit Database area (under Setup), scroll down to “Venues” and click “Venue constraints”. Then click the + Add venue category button in the top-right of the page or click an existing item.

For each constraint, you need to specify four things:
- Category: The venue category to which the subject of this constraint should be locked.
- Priority: This is a number used to resolve conflicts between constraints. Constraints with higher priority (greater number) take precedence over those with lower priority. If none of your constraints will ever conflict, then the priority is arbitrary (but it must still be specified).
- Subject content type: The type of subject to which this constraint relates: adjudicator, team, institution or division.
- Subject ID: Which adjudicator, team, institution or division the constraint relates to. The textbox takes a number (the ID of the object in the database), but you can search for the subject by clicking on the search icon next to it. This will bring up a table of objects of the type specified in “subject content type” for you to choose from. (You need to select the subject content type first.)

### Applying venue constraints
If you don’t have any venue constraints for adjudicators, venue constraints are applied automatically when the draw is generated.

However, if you have one or more venue constraints for adjudicators, it’s not possible to take adjudicator venue constraints into account during draw generation, because the adjudicator allocation isn’t known then. You’ll need to run the venue allocation yourself after you’ve allocated adjudicators.

To run venue allocation, go to Edit Venues (while looking at the draw), then in the screen where you can edit venues, click the Auto Allocate button. You can also do this at any other point (say, after adding a new venue constraint) if, for whatever reason, you would like to re-run the venue allocation algorithm.

If a venue constraint couldn’t be met, a message will show in the “conflicts/flags” column of the draw. A constraint might not be met for a number of reasons:
- It could be that constraints of different parties (say, one team and one adjudicator) conflicted, so only one could be fulfilled.
- It could be that all available rooms in the relevant category were already taken by other, higher-priority constraints.
- It could just be one of those edge cases that’s too hard for the naïve algorithm to handle.

Currently, Tabbycat doesn’t tell you which of these happened, so if the venue allocation fails to meet all your constraints, it’s on you to figure out why. In most scenarios, we imagine you’ll have few enough constraints that this will be obvious; for example, if the chief adjudicator is judging a team with accessibility requirements, it might be obvious that the latter’s constraint took priority. We might in future add support for more useful guidance on conflicting constraints, but we currently consider this to be of low priority.