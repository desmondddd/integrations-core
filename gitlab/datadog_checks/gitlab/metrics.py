# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

METRICS_MAP = {
    "gitlab_banzai_cached_render_real_duration_seconds": "banzai.cached_render_real_duration_seconds",
    "gitlab_banzai_cacheless_render_real_duration_seconds": "banzai.cacheless_render_real_duration_seconds",
    "gitlab_cache_misses_total": "cache.misses_total",
    "gitlab_cache_operation_duration_seconds": "cache.operation_duration_seconds",
    "gitlab_cache_operations_total": "cache_operations_total",
    "gitlab_database_transaction_seconds": "database.transaction_seconds",
    "gitlab_method_call_duration_seconds": "method_call_duration_seconds",
    "gitlab_page_out_of_bounds": "page_out_of_bounds",
    "gitlab_rails_queue_duration_seconds": "rails_queue_duration_seconds",
    "gitlab_sql_duration_seconds": "sql_duration_seconds",
    "gitlab_transaction_allocated_memory_bytes": "transaction.allocated_memory_bytes",
    "gitlab_transaction_cache_count_total": "transaction.cache_count_total",
    "gitlab_transaction_cache_duration_total": "transaction.cache_duration_total",
    "gitlab_transaction_cache_read_hit_count_total": "transaction.cache_read_hit_count_total",
    "gitlab_transaction_cache_read_miss_count_total": "transaction.cache_read_miss_count_total",
    "gitlab_transaction_duration_seconds": "transaction.duration_seconds",
    "gitlab_transaction_event_build_found_total": "transaction.event_build_found_total",
    "gitlab_transaction_event_build_invalid_total": "transaction.event_build_invalid_total",
    "gitlab_transaction_event_build_not_found_cached_total": "transaction.event_build_not_found_cached_total",
    "gitlab_transaction_event_build_not_found_total": "transaction.event_build_not_found_total",
    "gitlab_transaction_event_change_default_branch_total": "transaction.event_change_default_branch_total",
    "gitlab_transaction_event_create_repository_total": "transaction.event_create_repository_total",
    "gitlab_transaction_event_etag_caching_cache_hit_total": "transaction.event_etag_caching_cache_hit_total",
    "gitlab_transaction_event_etag_caching_header_missing_total": "transaction.event_etag_caching_header_missing_total",
    "gitlab_transaction_event_etag_caching_key_not_found_total": "transaction.event_etag_caching_key_not_found_total",
    "gitlab_transaction_event_etag_caching_middleware_used_total": "transaction.event_etag_caching_middleware_used_total",  # noqa
    "gitlab_transaction_event_etag_caching_resource_changed_total": "transaction.event_etag_caching_resource_changed_total",  # noqa
    "gitlab_transaction_event_fork_repository_total": "transaction.event_fork_repository_total",
    "gitlab_transaction_event_import_repository_total": "transaction.event_import_repository_total",
    "gitlab_transaction_event_push_branch_total": "transaction.event_push_branch_total",
    "gitlab_transaction_event_push_commit_total": "transaction.event_push_commit_total",
    "gitlab_transaction_event_push_tag_total": "transaction.event_push_tag_total",
    "gitlab_transaction_event_rails_exception_total": "transaction.event_rails_exception_total",
    "gitlab_transaction_event_receive_email_total": "transaction.event_receive_email_total",
    "gitlab_transaction_event_remote_mirrors_failed_total": "transaction.event_remote_mirrors_failed_total",
    "gitlab_transaction_event_remote_mirrors_finished_total": "transaction.event_remote_mirrors_finished_total",
    "gitlab_transaction_event_remote_mirrors_running_total": "transaction.event_remote_mirrors_running_total",
    "gitlab_transaction_event_remove_branch_total": "transaction.event_remove_branch_total",
    "gitlab_transaction_event_remove_repository_total": "transaction.event_remove_repository_total",
    "gitlab_transaction_event_remove_tag_total": "transaction.event_remove_tag_total",
    "gitlab_transaction_event_sidekiq_exception_total": "transaction.event_sidekiq_exception_total",
    "gitlab_transaction_event_stuck_import_jobs_total": "transaction.event_stuck_import_jobs_total",
    "gitlab_transaction_event_update_build_total": "transaction.event_update_build_total",
    "gitlab_transaction_new_redis_connections_total": "transaction.new_redis_connections_total",
    "gitlab_transaction_queue_duration_total": "transaction.queue_duration_total",
    "gitlab_transaction_rails_queue_duration_total": "transaction.rails_queue_duration_total",
    "gitlab_transaction_view_duration_total": "transaction.view_duration_total",
    "gitlab_view_rendering_duration_seconds": "view_rendering_duration_seconds",
    "http_requests_total": "rack.http_requests_total",
    "http_request_duration_seconds": "rack.http_request_duration_seconds",
    "pipelines_created_total": "pipelines_created_total",
    "rack_uncaught_errors_total": "rack.uncaught_errors_total",
    "user_session_logins_total": "user_session_logins_total",
    "upload_file_does_not_exist": "upload_file_does_not_exist",
    "failed_login_captcha_total": "failed_login_captcha_total",
    "successful_login_captcha_total": "successful_login_captcha_total",
    "auto_devops_pipelines_completed_total": "auto_devops_pipelines_completed_total",
    "sidekiq_jobs_cpu_seconds": "sidekiq.jobs_cpu_seconds",
    "sidekiq_jobs_completion_seconds": "sidekiq.jobs_completion_seconds",
    "sidekiq_jobs_queue_duration_seconds": "sidekiq.jobs_queue_duration_seconds",
    "sidekiq_jobs_failed_total": "sidekiq.jobs_failed_total",
    "sidekiq_jobs_retried_total": "sidekiq.jobs_retried_total",
    "sidekiq_running_jobs": "sidekiq.running_jobs",
    "sidekiq_concurrency": "sidekiq.concurrency",
    "ruby_gc_duration_seconds": "ruby.gc_duration_seconds",
    "ruby_file_descriptors": "ruby.file_descriptors",
    "ruby_memory_bytes": "ruby.memory_bytes",
    "ruby_sampler_duration_seconds_total": "ruby.sampler_duration_seconds_total",
    "ruby_process_cpu_seconds_total": "ruby.process_cpu_seconds_total",
    "ruby_process_max_fds": "ruby.process_max_fds",
    "ruby_process_resident_memory_bytes": "ruby.process_resident_memory_bytes",
    "ruby_process_start_time_seconds": "ruby.process_start_time_seconds",
    "ruby_gc_stat_count": "ruby.gc_stat.count",
    "ruby_gc_stat_heap_allocated_pages": "ruby.gc_stat.heap_allocated_pages",
    "ruby_gc_stat_heap_sorted_length": "ruby.gc_stat.heap_sorted_length",
    "ruby_gc_stat_heap_allocatable_pages": "ruby.gc_stat.heap_allocatable_pages",
    "ruby_gc_stat_heap_available_slots": "ruby.gc_stat.heap_available_slots",
    "ruby_gc_stat_heap_live_slots": "ruby.gc_stat.heap_live_slots",
    "ruby_gc_stat_heap_free_slots": "ruby.gc_stat.heap_free_slots",
    "ruby_gc_stat_heap_final_slots": "ruby.gc_stat.heap_final_slots",
    "ruby_gc_stat_heap_marked_slots": "ruby.gc_stat.heap_marked_slots",
    "ruby_gc_stat_heap_eden_pages": "ruby.gc_stat.heap_eden_pages",
    "ruby_gc_stat_heap_tomb_pages": "ruby.gc_stat.heap_tomb_pages",
    "ruby_gc_stat_total_allocated_pages": "ruby.gc_stat.total_allocated_pages",
    "ruby_gc_stat_total_freed_pages": "ruby.gc_stat.total_freed_pages",
    "ruby_gc_stat_total_allocated_objects": "ruby.gc_stat.total_allocated_objects",
    "ruby_gc_stat_total_freed_objects": "ruby.gc_stat.total_freed_objects",
    "ruby_gc_stat_malloc_increase_bytes": "ruby.gc_stat.malloc_increase_bytes",
    "ruby_gc_stat_malloc_increase_bytes_limit": "ruby.gc_stat.malloc_increase_bytes_limit",
    "ruby_gc_stat_minor_gc_count": "ruby.gc_stat.minor_gc_count",
    "ruby_gc_stat_major_gc_count": "ruby.gc_stat.major_gc_count",
    "ruby_gc_stat_remembered_wb_unprotected_objects": "ruby.gc_stat.remembered_wb_unprotected_objects",
    "ruby_gc_stat_remembered_wb_unprotected_objects_limit": "ruby.gc_stat.remembered_wb_unprotected_objects_limit",
    "ruby_gc_stat_old_objects": "ruby.gc_stat.old_objects",
    "ruby_gc_stat_old_objects_limit": "ruby.gc_stat.old_objects_limit",
    "ruby_gc_stat_oldmalloc_increase_bytes": "ruby.gc_stat.oldmalloc_increase_bytes",
    "ruby_gc_stat_oldmalloc_increase_bytes_limit": "ruby.gc_stat.oldmalloc_increase_bytes_limit",
    "geo_db_replication_lag_seconds": "geo.db_replication_lag_seconds",
    "geo_repositories": "geo.repositories",
    "geo_repositories_synced": "geo.repositories_synced",
    "geo_repositories_failed": "geo.repositories_failed",
    "geo_lfs_objects": "geo.lfs_objects",
    "geo_lfs_objects_synced": "geo.lfs_objects_synced",
    "geo_lfs_objects_failed": "geo.lfs_objects_failed",
    "geo_attachments": "geo.attachments",
    "geo_attachments_synced": "geo.attachments_synced",
    "geo_attachments_failed": "geo.attachments_failed",
    "geo_last_event_id": "geo.last_event_id",
    "geo_last_event_timestamp": "geo.last_event_timestamp",
    "geo_cursor_last_event_id": "geo.cursor_last_event_id",
    "geo_cursor_last_event_timestamp": "geo.cursor_last_event_timestamp",
    "geo_status_failed_total": "geo_status_failed_total",
    "geo_last_successful_status_check_timestamp": "geo.last_successful_status_check_timestamp",
    "geo_lfs_objects_synced_missing_on_primary": "geo.lfs_objects_synced_missing_on_primary",
    "geo_job_artifacts_synced_missing_on_primary": "geo.job_artifacts_synced_missing_on_primary",
    "geo_attachments_synced_missing_on_primary": "geo.attachments_synced_missing_on_primary",
    "geo_repositories_checksummed_count": "geo.repositories_checksummed_count",
    "geo_repositories_checksum_failed_count": "geo.repositories_checksum_failed_count",
    "geo_wikis_checksummed_count": "geo.wikis_checksummed_count",
    "geo_wikis_checksum_failed_count": "geo.wikis_checksum_failed_count",
    "geo_repositories_verified_count": "geo.repositories_verified_count",
    "geo_repositories_verification_failed_count": "geo.repositories_verification_failed_count",
    "geo_repositories_checksum_mismatch_count": "geo.repositories_checksum_mismatch_count",
    "geo_wikis_verified_count": "geo.wikis_verified_count",
    "geo_wikis_verification_failed_count": "geo.wikis_verification_failed_count",
    "geo_wikis_checksum_mismatch_count": "geo.wikis_checksum_mismatch_count",
    "geo_repositories_checked_count": "geo.repositories_checked_count",
    "geo_repositories_checked_failed_count": "geo.repositories_checked_failed_count",
    "geo_repositories_retrying_verification_count": "geo.repositories_retrying_verification_count",
    "geo_wikis_retrying_verification_count": "geo.wikis_retrying_verification_count",
    "db_load_balancing_hosts": "db_load_balancing_hosts",
    "unicorn_active_connections": "unicorn.active_connections",
    "unicorn_queued_connections": "unicorn.queued_connections",
    "unicorn_workers": "unicorn.workers",
    "puma_workers": "puma.workers",
    "puma_running_workers": "puma.running_workers",
    "puma_stale_workers": "puma.stale_workers",
    "puma_running": "puma.running",
    "puma_queued_connections": "puma.queued_connections",
    "puma_active_connections": "puma.active_connections",
    "puma_pool_capacity": "puma.pool_capacity",
    "puma_max_threads": "puma.max_threads",
    "puma_idle_threads": "puma.idle_threads",
    "puma_killer_terminations_total": "puma.killer_terminations_total",
}
