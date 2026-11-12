with events as (
    select * from {{ ref('seed_installation_events')}}
),

vessels as (
    select * from {{ ref('stg_vessels')}}
),

weather as (
    select * from {{ ref ('stg_weather_logs')}}
)

select 
    e.event_id,
    e.project_id,
    e.event_date,
    e.location,
    e.component_type,
    -- vessel info
    v.vessel_name,
    v.crane_capacity_t,
    -- meteorological info
    w.wave_height_m,
    w.wind_speed_kts,
    w.is_severe_weather,

    -- business logic: If severe adverse weather occurs, the entire installation duration is logged/classified as Weather Downtime.
    e.installation_duration_hours,
    case 
        when w.is_severe_weather = true then e.installation_duration_hours
        else 0
    end as weather_downtime_hours

from events e
left join vessels v
    on e.vessel_id = v.vessel_id
left join weather w
    on e.event_date=w.log_date
    and e.location = w.location

