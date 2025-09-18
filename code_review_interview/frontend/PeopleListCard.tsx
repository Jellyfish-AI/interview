import React from 'react';
import { useNavigate } from 'react-router-dom';

type PeopleListCardProps = {
  person: any;
};

export const PeopleListCard: React.FC<PeopleListCardProps> = (props) => {
  const navigate = useNavigate();

  return (
    <div style={{ marginTop: '24px' }} onClick={() => navigate(`/person/${props.person.id}`)}>
      <div>{props.person.name}</div>
      <div>Team: {props.person.team?.name}</div>
      <div style={{ backgroundColor: props.person.engineerType.color, color: 'white' }}>
        {props.person.engineerType.label}
      </div>
    </div>
  );
};
