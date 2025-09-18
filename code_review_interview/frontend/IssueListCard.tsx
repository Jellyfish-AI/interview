import React from 'react';

import { Issue } from './types';

type IssueListCardProps = {
  issue: Issue;
};

export const IssueListCard: React.FC<IssueListCardProps> = (props) => {
  return (
    <div>
      <div>{props.issue.title}</div>
      <div>Team: {props.issue.team.name}</div>
    </div>
  );
};
