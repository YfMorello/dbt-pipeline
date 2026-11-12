with source as (
    select * from {{ ref('seed_vessels')}}
),

renamed as (
    select
        vessel_id,
        vessel_name,
        imo_number,
        crane_capacity_tonnes as crane_capacity_t,
        upper(status) as vessel_status
    from source
)

select * from renamed