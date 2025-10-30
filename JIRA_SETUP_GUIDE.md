# EventLync Jira Setup Guide
# Complete step-by-step instructions for setting up your team project

## Step 1: Create Your Jira Project

### 1.1 Sign up/Login to Jira
```
Go to: https://www.atlassian.com/software/jira
- Sign up for a free account (or login if you have one)
- Choose "Jira Work Management" for software teams
- Select "Team-managed" project (easier for beginners)
```

### 1.2 Create New Project
```
Project Name: EventLync Development
Project Key: ELYNC (or EVNT)
Template: Basic software development
```

## Step 2: Set Up Your Team Board

### 2.1 Create Epics (Main Categories)
For each developer, create an Epic:

```
Epic 1: [EPIC] Authentication & User Management
Epic 2: [EPIC] Events & Tickets Management  
Epic 3: [EPIC] Orders & Payments System
```

### 2.2 Create Stories Under Each Epic
Use the detailed story templates I provided earlier.

## Step 3: Jira Workflow Basics

### 3.1 Board Columns (Kanban Style)
```
Backlog → To Do → In Progress → In Review → Done
```

### 3.2 Issue Types
```
Epic: Large feature/category
Story: User functionality 
Task: Technical work
Bug: Code fixes needed
Subtask: Smaller work items
```

## Step 4: Quick Setup Checklist

### ✅ Must-Do First:
1. **Create Jira account** at atlassian.com
2. **Create "EventLync Development" project**
3. **Set up basic board** (Backlog, To Do, In Progress, Done)
4. **Create the 3 Epics** (one per developer)
5. **Add team members** to the project

### ✅ Add Team Members:
```
Project Settings → People → Add team members
- Give them appropriate roles (Member/Developer)
- Share the project link with your team
```

### ✅ Create Issues:
```
For each developer:
1. Create their Epic first
2. Create Stories under that Epic
3. Assign the Epic to the developer
4. Add story points and priorities
```

## Step 5: Daily Workflow

### For Team Members:
```
1. Check "To Do" column for assigned tasks
2. Move to "In Progress" when starting work
3. Create pull request when ready for review
4. Move to "In Review" during code review
5. Move to "Done" when merged and tested
```

### For You (Project Manager):
```
1. Create new issues as needed
2. Monitor progress in the board
3. Update priorities as requirements change
4. Review pull requests and move issues
```

## Step 6: Alternative Simple Approach

If Jira feels overwhelming, try **GitHub Projects** instead:

### GitHub Projects Setup:
```
1. Go to your GitHub repo
2. Click "Projects" tab
3. Create new project: "EventLync Development"
4. Use "Basic kanban" template
5. Create columns: Backlog, To Do, In Progress, Review, Done
6. Add issues using the templates I provided
7. Assign team members to issues
```

## Step 7: Communication Setup

### Daily Standups:
```
Use Discord/Slack channel: #eventlync-daily
Format:
- What did you work on yesterday?
- What will you work on today?
- Any blockers?
```

### Code Reviews:
```
- Use GitHub pull requests
- Require at least 1 approval
- Use the review checklist I provided
```

## Step 8: Quick Start Template

Here's a minimal Jira setup you can copy:

### Issues to Create:
```
1. Epic: [EPIC] Auth System - Developer 1
   ├── Story: Backend Auth API
   ├── Story: Frontend Auth UI
   └── Story: User Profile Management

2. Epic: [EPIC] Events System - Developer 2  
   ├── Story: Event CRUD Backend
   ├── Story: Ticket Management
   └── Story: Event UI Frontend

3. Epic: [EPIC] Payments System - Developer 3
   ├── Story: Order Processing
   ├── Story: M-Pesa Integration  
   └── Story: Check-in System
```

## Step 9: Common Jira Questions

### Q: How do I assign work?
```
Click issue → Assignee field → Select team member
```

### Q: How do I track time?
```
Issue view → Time tracking → Log work
Or just update status: To Do → In Progress → Done
```

### Q: How do I add subtasks?
```
Issue view → More → Create subtask
```

### Q: How do I create a sprint?
```
If using Scrum: Backlog → Create sprint → Add issues → Start sprint
```

### Q: How do I filter issues?
```
Board view → Filters → Assignee/Member/etc.
```

## Step 10: If Jira Still Feels Too Complex

### Option A: Use Trello (Free & Simple)
```
1. Create board: "EventLync Development"
2. Create lists: Backlog, To Do, In Progress, Review, Done
3. Add cards with issue descriptions
4. Assign team members to cards
5. Use checklists for subtasks
```

### Option B: Use GitHub Issues + Projects
```
1. Use GitHub Issues for tasks
2. Use GitHub Projects for board view
3. Labels for categorization
4. Assignments for team members
```

## Step 11: Success Checklist

- [ ] Jira project created
- [ ] Team members added
- [ ] 3 Epics created (one per developer)
- [ ] Stories created under epics
- [ ] Board columns set up
- [ ] Issues assigned to team members
- [ ] Communication channel established
- [ ] Daily standup process defined

## Need Help?

If you get stuck on any step:
1. **Take a screenshot** of where you're stuck
2. **Describe what you expected** vs what happened
3. **I'll guide you through it** step by step

**What's your first question about Jira setup?** 🤔
