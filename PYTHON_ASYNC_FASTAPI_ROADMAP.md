# Python Asyncio + FastAPI — Interview Practice Tracker

**Target:** Senior / Staff / Principal Engineer at product-based companies  
**Approach:** One topic at a time. For each item: explain it, implement it, test edge cases, and discuss production trade-offs.

## 1. Python Fundamentals
- [ ] Python execution model and call stack
- [ ] Functions, arguments, `*args`, `**kwargs`
- [ ] Mutable vs immutable objects
- [ ] References, shallow copy, deep copy
- [ ] Collections: list, tuple, set, dict
- [ ] Comprehensions and iterators
- [ ] Generators and `yield`
- [ ] Decorators and closures
- [ ] Context managers and `with`
- [ ] Exceptions and custom exceptions
- [ ] Type hints, generics, protocols
- [ ] Dataclasses and Pydantic models
- [ ] Object-oriented programming and MRO
- [ ] Reference counting and garbage collection

## 2. Processes, Threads, and Concurrency
- [ ] Process vs thread vs coroutine
- [ ] Concurrency vs parallelism
- [ ] I/O-bound vs CPU-bound tasks
- [ ] Blocking vs non-blocking execution
- [ ] `threading.Thread`
- [ ] `ThreadPoolExecutor` and `ProcessPoolExecutor`
- [ ] GIL and free-threaded CPython considerations
- [ ] Context switching and thread overhead
- [ ] Shared memory and thread-local storage
- [ ] Multiprocessing and inter-process communication
- [ ] Thread safety vs async safety

## 3. Asyncio Fundamentals
- [ ] Event loop and lifecycle
- [ ] Coroutines and coroutine objects
- [ ] `async def` and `await`
- [ ] Awaitables: coroutine, Task, Future
- [ ] `asyncio.run()`
- [ ] `asyncio.sleep()` vs `time.sleep()`
- [ ] Sequential vs concurrent execution
- [ ] `asyncio.create_task()`
- [ ] Task lifecycle, scheduling, and references
- [ ] `asyncio.gather()`
- [ ] `asyncio.TaskGroup`
- [ ] `asyncio.wait()` and `as_completed()`
- [ ] Async iterators and generators
- [ ] Async context managers
- [ ] `contextvars` and context propagation

## 4. Synchronization and Concurrency Problems
- [ ] Race conditions and lost updates
- [ ] Critical sections and atomicity
- [ ] Mutex and mutual exclusion
- [ ] `asyncio.Lock` vs `threading.Lock`
- [ ] RLock and reentrancy
- [ ] Semaphore vs bounded semaphore
- [ ] Condition variables
- [ ] Events and coordination
- [ ] Barriers
- [ ] Deadlocks and lock ordering
- [ ] Livelock, starvation, fairness
- [ ] Priority inversion
- [ ] Optimistic vs pessimistic concurrency
- [ ] Cross-process and distributed synchronization

## 5. Producer–Consumer and Backpressure
- [ ] Producer–Consumer problem
- [ ] `asyncio.Queue(maxsize=N)`
- [ ] `put()`, `get()`, `task_done()`, `join()`
- [ ] Multiple producers and consumers
- [ ] Bounded vs unbounded queues
- [ ] Worker pools and concurrency limits
- [ ] Queue capacity and Little's Law
- [ ] Backpressure and producer suspension
- [ ] Backpressure vs rate limiting
- [ ] Backpressure vs admission control
- [ ] Backpressure vs load shedding
- [ ] Queue overflow and rejection policies
- [ ] FIFO vs priority queues
- [ ] Queue shutdown and sentinel patterns
- [ ] Cancellation during queue processing
- [ ] Slow consumers and head-of-line blocking
- [ ] Queue depth, wait time, saturation metrics

## 6. Cancellation, Timeouts, and Structured Concurrency
- [ ] Task cancellation lifecycle
- [ ] `asyncio.CancelledError`
- [ ] `try/finally` cleanup
- [ ] Cancellation propagation
- [ ] `TaskGroup` failure semantics
- [ ] `ExceptionGroup` and `except*`
- [ ] `gather()` vs `TaskGroup` failures
- [ ] `asyncio.timeout()`
- [ ] `asyncio.wait_for()`
- [ ] Per-operation timeout vs overall deadline
- [ ] Deadline propagation
- [ ] `asyncio.shield()`
- [ ] Timeout vs cancellation vs provider failure
- [ ] Orphaned tasks and task leaks
- [ ] Cancellation-safe resource management
- [ ] Graceful task shutdown

## 7. Asyncio and Thread Integration
- [ ] `asyncio.to_thread()`
- [ ] `loop.run_in_executor()`
- [ ] `loop.call_soon_threadsafe()`
- [ ] `asyncio.run_coroutine_threadsafe()`
- [ ] Blocking synchronous libraries in async code
- [ ] Thread pool saturation and sizing
- [ ] Executor lifecycle
- [ ] GIL implications for CPU workloads
- [ ] CPU-bound processing with processes
- [ ] Context propagation to threads
- [ ] Cancellation limitations of thread work

## 8. HTTP and Networking
- [ ] Client–server architecture
- [ ] DNS, IP, ports, sockets
- [ ] TCP connections and handshake
- [ ] HTTP request and response lifecycle
- [ ] GET, POST, PUT, PATCH, DELETE
- [ ] HTTP status codes
- [ ] Headers, query parameters, request bodies
- [ ] HTTP/1.1 vs HTTP/2
- [ ] Keep-alive and connection reuse
- [ ] Connection pooling
- [ ] TCP vs WebSockets
- [ ] TLS and HTTPS
- [ ] Connect, read, write, and pool timeouts
- [ ] Client disconnects and retries
- [ ] HTTP idempotency semantics

## 9. FastAPI Fundamentals
- [ ] FastAPI vs asyncio vs ASGI
- [ ] FastAPI, Starlette, AnyIO, Uvicorn
- [ ] Create a FastAPI application
- [ ] Path operations and decorators
- [ ] Path and query parameters
- [ ] Request bodies and validation
- [ ] Pydantic `BaseModel`
- [ ] Response models and serialization
- [ ] `HTTPException` and error handling
- [ ] Dependency injection with `Depends`
- [ ] Async vs sync endpoints
- [ ] Request and response objects
- [ ] Headers and cookies
- [ ] Middleware and execution order
- [ ] `APIRouter` and project structure
- [ ] OpenAPI and Swagger documentation
- [ ] Pagination, filtering, sorting
- [ ] File uploads and multipart requests
- [ ] API versioning

## 10. Advanced FastAPI and Runtime
- [ ] ASGI scope, receive, send
- [ ] Uvicorn event loop and worker architecture
- [ ] Sync endpoints and thread-pool execution
- [ ] Blocking the event loop
- [ ] Application lifespan management
- [ ] Startup/shutdown resource initialization
- [ ] Shared HTTP clients and DB pools
- [ ] Dependency caching and scopes
- [ ] `BackgroundTasks` and limitations
- [ ] `StreamingResponse`
- [ ] Server-Sent Events (SSE)
- [ ] WebSockets and connection lifecycle
- [ ] Slow-client backpressure
- [ ] Client disconnect detection
- [ ] Request cancellation and deadlines
- [ ] Application state vs request state
- [ ] Multi-worker state isolation
- [ ] Graceful shutdown with active requests

## 11. Database and Persistence
- [ ] Sync vs async database drivers
- [ ] Async SQLAlchemy
- [ ] Database sessions and lifecycle
- [ ] Connection pooling and exhaustion
- [ ] Transactions and rollback
- [ ] ACID properties
- [ ] Transaction isolation levels
- [ ] Lost updates and write conflicts
- [ ] Optimistic vs pessimistic locking
- [ ] `SELECT FOR UPDATE`
- [ ] Database deadlocks
- [ ] Idempotent writes and idempotency keys
- [ ] N+1 queries and query optimization
- [ ] Database migrations
- [ ] Redis caching and atomic operations
- [ ] Outbox pattern

## 12. API Security
- [ ] Authentication vs authorization
- [ ] OAuth2 and OpenID Connect
- [ ] JWT validation, expiration, key rotation
- [ ] RBAC and ABAC
- [ ] Dependency-based authorization
- [ ] CORS and CSRF
- [ ] Input validation and injection prevention
- [ ] SQL injection
- [ ] SSRF and unsafe outbound requests
- [ ] Secrets management
- [ ] PII redaction and sensitive logging
- [ ] TLS and secure transport
- [ ] Rate limiting and abuse protection
- [ ] Request-size and upload limits
- [ ] Multi-tenant isolation

## 13. Reliability and Resilience
- [ ] Retries and exponential backoff
- [ ] Jitter and retry budgets
- [ ] Circuit breaker pattern
- [ ] Bulkhead isolation
- [ ] Token bucket and sliding-window rate limiting
- [ ] Concurrency limiting
- [ ] Admission control and overload rejection
- [ ] Load shedding
- [ ] Timeout and deadline budgets
- [ ] Fallback strategies
- [ ] Idempotency and duplicate requests
- [ ] Resource exhaustion
- [ ] Partial failures and failure isolation
- [ ] Graceful degradation
- [ ] Graceful shutdown and recovery

## 14. Distributed Systems and Messaging
- [ ] In-memory vs durable queues
- [ ] RabbitMQ, Kafka, Redis Streams
- [ ] At-most-once vs at-least-once delivery
- [ ] Duplicate processing and deduplication
- [ ] Message acknowledgments and retries
- [ ] Dead-letter queues
- [ ] Ordering guarantees and partitions
- [ ] Consumer groups and scaling
- [ ] Distributed locks and leases
- [ ] Leader election basics
- [ ] Consistency and availability trade-offs
- [ ] Outbox and saga patterns
- [ ] Long-running jobs and checkpointing
- [ ] Crash recovery and worker restart
- [ ] Distributed backpressure

## 15. Testing and Debugging
- [ ] pytest fundamentals
- [ ] pytest-asyncio
- [ ] HTTPX `AsyncClient` and `ASGITransport`
- [ ] FastAPI dependency overrides
- [ ] Unit vs integration vs contract tests
- [ ] Mocking async functions
- [ ] Deterministic race-condition tests
- [ ] Testing locks and semaphores
- [ ] Testing cancellation propagation
- [ ] Testing timeouts and deadlines
- [ ] Testing Producer–Consumer queues
- [ ] Testing graceful shutdown
- [ ] Fault injection and provider failures
- [ ] Concurrency stress tests
- [ ] Load testing with Locust or k6
- [ ] Debugging task leaks and blocked event loops

## 16. Performance and Observability
- [ ] Latency vs throughput
- [ ] p50, p95, p99 latency
- [ ] Queue waiting time vs processing time
- [ ] Event-loop lag
- [ ] CPU and memory profiling
- [ ] Async task and thread monitoring
- [ ] Connection pool metrics
- [ ] Queue depth and saturation
- [ ] Structured logging
- [ ] Correlation and request IDs
- [ ] OpenTelemetry tracing
- [ ] Prometheus metrics
- [ ] Distributed tracing
- [ ] Little's Law and capacity planning
- [ ] Horizontal scaling and worker sizing
- [ ] Kubernetes readiness and liveness probes
- [ ] Resource limits and autoscaling
- [ ] Performance bottleneck analysis

## 17. Agentic AI and LLM API Engineering
- [ ] Async LLM provider calls
- [ ] Parallel tool execution
- [ ] Multi-provider routing and fallback
- [ ] Provider-specific concurrency limits
- [ ] Token and request rate limits
- [ ] Streaming LLM responses via SSE
- [ ] Cancellation of expensive LLM calls
- [ ] Overall request deadline management
- [ ] Async RAG retrieval and reranking
- [ ] Tool-call timeout and retry handling
- [ ] Long-running agent workflows
- [ ] Agent checkpointing and recovery
- [ ] Cost and token usage tracking
- [ ] AI Gateway backpressure
- [ ] Prompt and tool security
- [ ] Multi-tenant isolation and quotas
- [ ] Observability and tracing for agents

## 18. Hands-on Coding and Design Challenges
- [ ] Implement a bounded Producer–Consumer queue
- [ ] Reproduce and fix an asyncio race condition
- [ ] Implement a concurrency-safe counter
- [ ] Implement a semaphore-based worker pool
- [ ] Build an async rate limiter
- [ ] Implement a deadline-aware API aggregator
- [ ] Build retry and circuit breaker utilities
- [ ] Design a graceful shutdown mechanism
- [ ] Diagnose event-loop blocking
- [ ] Explain how to handle 10,000 concurrent connections
- [ ] Design a high-throughput FastAPI service
- [ ] Design a distributed background job processor
- [ ] Design a resilient AI Gateway
- [ ] Conduct a performance and failure-mode review
- [ ] Explain architecture trade-offs and operational SLOs

---

## Practice Log

| Date | Topic | Code / PR | Tests | Production trade-offs | Status |
|---|---|---|---|---|---|
| | | | | | Not started |

## Completion Criteria

Mark a checkbox only after you can:
1. Explain the concept without notes.
2. Implement a minimal working example.
3. Test a failure mode or edge case.
4. Explain trade-offs and operational behavior.

## Official References

- [Python asyncio](https://docs.python.org/3.14/library/asyncio.html)
- [Python threading](https://docs.python.org/3.14/library/threading.html)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Starlette documentation](https://www.starlette.io/)
- [Uvicorn documentation](https://www.uvicorn.org/)
- [Pydantic documentation](https://docs.pydantic.dev/)
