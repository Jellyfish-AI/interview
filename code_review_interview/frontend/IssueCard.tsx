import React from 'react';

import { Issue } from './types';

type IssueCardProps = {
  issue: Issue;
};

export const IssueCard: React.FC<IssueCardProps> = (props) => {
  return (
    <div>
      <div>{props.issue.title}</div>
      <div>Team: {props.issue.team.name}</div>
    </div>
  );
};
