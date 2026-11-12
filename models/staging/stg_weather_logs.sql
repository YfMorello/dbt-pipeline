with source as(
    select * from {{ ref('seed_weather_logs')}}

),

renamed as (
    select 
        cast(log_date as date) as log_date,
        location,
        wave_height_m,
        wind_speed_kts,
        -- if wave_height > 2.2m or wind_speed > 25 kts is abnormal
        case
            when wave_height_m > 2.2 or wind_speed_kts > 25.0 then true
            else false
        end as is_severe_weather
    from source
        )  
select * from renamed
