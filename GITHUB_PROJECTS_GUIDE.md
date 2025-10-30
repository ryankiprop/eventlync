# EventLync GitHub Projects Setup (SIMPLER Alternative)

## Why GitHub Projects Instead of Jira?

✅ **Already connected** to your repository  
✅ **Free** (unlike Jira paid plans)  
✅ **Simple interface** - less overwhelming  
✅ **Integrated** with GitHub PRs and issues  
✅ **No separate login** required  

## Step 1: Create GitHub Project

### 1.1 Go to Your Repository
```
Navigate to: https://github.com/ryankiprop/eventlync
```

### 1.2 Create New Project
```
1. Click "Projects" tab (next to "Code", "Issues", "Pull requests")
2. Click "New project"
3. Choose "Basic kanban" template
4. Project name: "EventLync Development"
5. Description: "Team task management for EventLync platform"
6. Click "Create project"
```

## Step 2: Set Up Your Board Columns

### Default Columns (Edit if needed):
```
Backlog → To Do → In Progress → Review → Done
```

### 2.1 Customize Columns (Optional)
```
Click "..." next to column name → Edit column name
Suggested columns:
- Backlog (planning)
- To Do (ready to work)
- In Progress (actively working)
- In Review (code review/pull request)
- Done (completed and tested)
```

## Step 3: Create Issues for Each Developer

### 3.1 Create Epic-Style Issues
For each developer, create a main "Epic" issue:

#### Developer 1: Authentication & User Management
```
Title: 🎯 [EPIC] Authentication & User Management - Developer 1
Description:
## Overview
Handle user registration, login, JWT tokens, and user management.

## Stories to Complete:
- [ ] Backend Auth API (register, login, JWT)
- [ ] Frontend Auth UI (forms, context, protected routes)
- [ ] User Profile Management

## Time Estimate: 14-18 hours
## Priority: High

## Resources:
- Team Guide: https://github.com/ryankiprop/eventlync/blob/main/TEAM_GUIDE.md#developer-1-authentication--user-management
- Backend Code: backend/app/routes/auth.py
- Frontend Code: frontend/src/context/AuthContext.jsx
```

#### Developer 2: Events & Tickets Management
```
Title: 🎯 [EPIC] Events & Tickets Management - Developer 2
Description:
## Overview
Event CRUD, ticket management, file uploads, and analytics.

## Stories to Complete:
- [ ] Backend Events CRUD (create, read, update, delete)
- [ ] Backend Tickets Management (types, availability, pricing)
- [ ] File Upload System (Cloudinary integration)
- [ ] Frontend Event Management UI

## Time Estimate: 18-22 hours
## Priority: High

## Resources:
- Team Guide: https://github.com/ryankiprop/eventlync/blob/main/TEAM_GUIDE.md#developer-2-events--tickets-management
- Backend Code: backend/app/routes/events.py, tickets.py
- Frontend Code: frontend/src/pages/organizer/, components/events/
```

#### Developer 3: Orders & Payments
```
Title: 🎯 [EPIC] Orders & Payments System - Developer 3
Description:
## Overview
Order processing, M-Pesa integration, QR codes, check-in system.

## Stories to Complete:
- [ ] Backend Order Management
- [ ] M-Pesa Payment Integration
- [ ] QR Code Check-in System
- [ ] Frontend Payment & Check-in UI

## Time Estimate: 20-25 hours
## Priority: Critical

## Resources:
- Team Guide: https://github.com/ryankiprop/eventlync/blob/main/TEAM_GUIDE.md#developer-3-orders--payments
- Backend Code: backend/app/routes/orders.py, payments.py, utils/mpesa.py
- Frontend Code: frontend/src/services/payments.js, pages/user/Orders.jsx
```

### 3.2 Create Detailed Story Issues
For each main story, create separate issues:

```
Example Story Issue:

Title: 🔧 Backend Auth API Implementation
Description:
## Objective
Implement complete authentication system including registration, login, and JWT tokens.

## Tasks
- [ ] Add RegisterResource.post() in backend/app/routes/auth.py
- [ ] Add LoginResource.post() with JWT generation
- [ ] Add MeResource.get() for user profile
- [ ] Configure JWT_SECRET_KEY in config.py
- [ ] Add password hashing with bcrypt

## API Endpoints
- POST /api/auth/register
- POST /api/auth/login
- GET /api/auth/me

## Acceptance Criteria
- [ ] Users can register successfully
- [ ] Login returns valid JWT tokens
- [ ] Passwords are securely hashed
- [ ] JWT tokens include user roles

## Testing
- [ ] Test registration flow
- [ ] Test login and token generation
- [ ] Test protected endpoints

## Related Files
- backend/app/routes/auth.py
- backend/app/models/user.py
- backend/config.py
```

## Step 4: Assign Team Members

### 4.1 Assign Epic Owners
```
1. Open each Epic issue
2. Click "Assignees" on the right
3. Select the appropriate developer
```

### 4.2 Add Labels for Organization
```
Create these labels:
- developer-1 (blue)
- developer-2 (green)  
- developer-3 (orange)
- backend (red)
- frontend (purple)
- high-priority (red)
- medium-priority (yellow)
- low-priority (green)
```

## Step 5: Set Up Automation (Optional)

### 5.1 Auto-move Issues
```
Project Settings → Workflows
Enable: "Auto-add to project" for new issues
```

### 5.2 Link to Pull Requests
```
When creating PRs, reference issue numbers:
"Fixes #123" or "Closes #123"
This will auto-move issues when PR is merged
```

## Step 6: Daily Workflow

### For Developers:
```
1. Check "To Do" column for your assigned issues
2. Drag issue to "In Progress" when starting
3. Work on the task, commit to feature branch
4. Create pull request when ready
5. Move issue to "Review" during PR review
6. Issue moves to "Done" when PR is merged
```

### For You (Project Manager):
```
1. Monitor the board daily
2. Create new issues as needed
3. Review pull requests
4. Help unblock team members
5. Update priorities as needed
```

## Step 7: Communication

### Use GitHub Discussions or Issues for:
- Daily standup updates
- Blocker notifications
- Design decisions
- Code review feedback

### Format for Daily Updates:
```
## Daily Standup - [Date]

### What I worked on yesterday:
- Completed backend auth API
- Started frontend login form

### What I'll work on today:
- Finish login form validation
- Test auth integration

### Blockers:
- Need clarification on JWT refresh tokens
```

## Step 8: Progress Tracking

### Use Checklists in Issues
```
- [x] Task completed
- [ ] Task in progress
- [ ] Task not started
```

### View Progress
```
Project Board → View all issues with status
Use filters: assignee, label, status
```

## Step 9: Success Metrics

- [ ] GitHub Project created and configured
- [ ] 3 Epic issues created and assigned
- [ ] Story issues created under epics
- [ ] Team members can access the project
- [ ] Workflow is understood by all
- [ ] First issues moved to "In Progress"

## Quick Start Checklist

1. ✅ Go to https://github.com/ryankiprop/eventlync/projects
2. ✅ Click "New project" → "Basic kanban"
3. ✅ Name it "EventLync Development"
4. ✅ Create the 3 Epic issues above
5. ✅ Assign developers to their epics
6. ✅ Add team members to the repository
7. ✅ Share the project link with the team

## Need Help?

**Send me a screenshot** of where you're stuck, and I'll guide you through it!

**Ready to start? What's your first step?** 🚀
