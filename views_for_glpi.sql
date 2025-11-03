-- glpi.lexa_interfaces source

CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `lexa_interfaces` AS
select
    `glpi_computers`.`id` AS `pcid`,
    `glpi_computers`.`name` AS `hostname`,
    `glpi_ipaddresses`.`name` AS `ip`,
    `glpi_networks`.`name` AS `subnet`,
    `glpi_states`.`name` AS `status`
from
    (((`glpi_computers`
left join `glpi_ipaddresses` on
    (`glpi_computers`.`id` = `glpi_ipaddresses`.`mainitems_id`))
left join `glpi_networks` on
    (`glpi_computers`.`networks_id` = `glpi_networks`.`id`))
left join `glpi_states` on
    (`glpi_computers`.`states_id` = `glpi_states`.`id`))    
where
    `glpi_computers`.`is_deleted` <> '1'
    and `glpi_ipaddresses`.`version` = '4'
    and `glpi_ipaddresses`.`name` <> '127.0.0.1'
group by
    `glpi_computers`.`name`;

-- glpi.lexa_oss source

CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `lexa_oss` AS
select
    `glpi_items_operatingsystems`.`items_id` AS `items_id`,
    `glpi_items_operatingsystems`.`operatingsystems_id` AS `operatingsystems_id`
from
    (`glpi_items_operatingsystems`
join `glpi_computers` on
    (`glpi_computers`.`id` = `glpi_items_operatingsystems`.`items_id`));

-- glpi.lexa_os_by_host source

CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `lexa_os_by_host` AS
select
    `lexa_oss`.`items_id` AS `items_id`,
    `glpi_operatingsystems`.`name` AS `name`
from
    (`lexa_oss`
join `glpi_operatingsystems` on
    (`lexa_oss`.`operatingsystems_id` = `glpi_operatingsystems`.`id`));

-- glpi.lexa_users source

CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `lexa_users` AS
select
    `glpi_users`.`id` AS `id`,
    concat(`glpi_users`.`firstname`, ' ', `glpi_users`.`realname`) AS `fullname`,
    `glpi_users`.`mobile` AS `mobile`,
    `glpi_useremails`.`email` AS `email`
from
    (`glpi_users`
left join `glpi_useremails` on
    (`glpi_users`.`id` = `glpi_useremails`.`users_id`));

-- glpi.lexa_rundeck source

CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `lexa_rundeck` AS
select
    `lexa_interfaces`.`pcid` AS `pcid`,
    `lexa_interfaces`.`hostname` AS `hostname`,
    `lexa_interfaces`.`ip` AS `ip`,
    `lexa_interfaces`.`subnet` AS `subnet`,
    `lexa_os_by_host`.`name` AS `os_name`,
    `lexa_interfaces`.`status` AS `status`
from
    ((`lexa_interfaces`
join `lexa_oss` on
    (`lexa_interfaces`.`pcid` = `lexa_oss`.`items_id`))
join `lexa_os_by_host` on
    (`lexa_interfaces`.`pcid` = `lexa_os_by_host`.`items_id`));

-- glpi.lexa_computers source

CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `lexa_computers` AS
select
    `glpi_computers`.`name` AS `host_name`,
    `glpi_computers`.`comment` AS `description`,
    `glpi_plugin_fields_computerlexas`.`notmonitoredfield` AS `disabled`,
    `glpi_locations`.`name` AS `location`,
    `glpi_locations`.`latitude` AS `location_lat`,
    `glpi_locations`.`longitude` AS `location_lon`,
    `glpi_groups`.`name` AS `poc_2_name`,
    `lexa_users`.`fullname` AS `contact`,
    `lexa_users`.`fullname` AS `poc_1_name`,
    `lexa_users`.`email` AS `poc_1_email`,
    `lexa_users`.`mobile` AS `poc_1_cell`,
    `glpi_computertypes`.`name` AS `type`,
    `glpi_computermodels`.`name` AS `hardware`,
    `lexa_os_by_host`.`name` AS `os`,
    `glpi_computers`.`name` AS `name`,
    `glpi_plugin_fields_computerlexas`.`fqdnfield` AS `interface_dns`,
    `glpi_plugin_fields_computerlexas`.`visiblenamealiasfield` AS `visible_name`,
    `glpi_plugin_fields_computerlexas`.`visiblenamealiasfield` AS `alias`,
    `glpi_plugin_fields_computerlexas`.`interfacedefaultfield` AS `interface_default`,
    `glpi_plugin_fields_computerlexas`.`plugin_fields_interfacetypefielddropdowns_id` AS `interface_type`,
    `glpi_plugin_fields_computerlexas`.`portfield` AS `interface_port`,
    `glpi_plugin_fields_computerlexas`.`useipfield` AS `interface_use_ip`,
    `glpi_plugin_fields_computerlexas`.`realipfield` AS `interface_ip_address`,
    `glpi_plugin_fields_computerlexas`.`insertedinzabbixfield` AS `inserted`,
    `glpi_plugin_fields_computerlexas`.`updatedfield` AS `updated`,
    `glpi_computers`.`is_deleted` AS `deleted`
from
    ((((((((`glpi_computers`
join `glpi_locations` on
    (`glpi_computers`.`locations_id` = `glpi_locations`.`id`))
left join `lexa_users` on
    (`glpi_computers`.`users_id_tech` = `lexa_users`.`id`))
left join `glpi_groups` on
    (`glpi_computers`.`groups_id_tech` = `glpi_groups`.`id`))
left join `glpi_computertypes` on
    (`glpi_computers`.`computertypes_id` = `glpi_computertypes`.`id`))
left join `glpi_computermodels` on
    (`glpi_computers`.`computermodels_id` = `glpi_computermodels`.`id`))
left join `glpi_plugin_fields_computerlexas` on
    (`glpi_computers`.`id` = `glpi_plugin_fields_computerlexas`.`items_id`))
left join `lexa_interfaces` on
    (`glpi_computers`.`id` = `lexa_interfaces`.`pcid`))
left join `lexa_os_by_host` on
    (`glpi_computers`.`id` = `lexa_os_by_host`.`items_id`));
